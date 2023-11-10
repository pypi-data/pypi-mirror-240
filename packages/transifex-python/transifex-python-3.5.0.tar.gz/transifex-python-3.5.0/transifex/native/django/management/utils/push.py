from __future__ import absolute_import, unicode_literals

import os
import sys
import time

from django import VERSION as DJANGO_VERSION
from django.conf import settings
from django.core.management.utils import handle_extensions
from transifex.common.console import Color
from transifex.common.utils import generate_hashed_key, generate_key
from transifex.native import tx
from transifex.native.django.management.common import SourceStringCollection
from transifex.native.django.management.utils.base import CommandMixin
from transifex.native.django.utils.templates import \
    extract_transifex_template_strings
from transifex.native.parsing import Extractor

if DJANGO_VERSION[0] >= 4:
    from django.utils.encoding import force_str as force_text
else:
    from django.utils.encoding import force_text


class Push(CommandMixin):
    def add_arguments(self, subparsers):
        parser = subparsers.add_parser(
            'push',
            help=("Detect translatable strings in Django templates and Python "
                  "files and push them as source strings to Transifex"),
        )
        parser.add_argument(
            '--extension', '-e', dest='extensions', action='append',
            help=('The file extension(s) to examine (default: "html,txt,py", '
                  'or "js" if the domain is "djangojs"). Separate multiple '
                  'extensions with commas, or use -e multiple times.'),
        )
        parser.add_argument(
            '--purge', '-p', action='store_true', dest='purge', default=False,
            help=('Replace the entire resource content with the '
                  'pushed content of this request. If not provided (the '
                  'default), then append the source content of this request '
                  'to the existing resource content.'),
        )
        parser.add_argument(
            '--append-tags', dest='append_tags', default=None,
            help=('Append tags to strings when pushing to Transifex'),
        )
        parser.add_argument(
            '--with-tags-only', dest='with_tags_only', default=None,
            help=('Push only strings that contain specific tags'),
        )
        parser.add_argument(
            '--without-tags-only', dest='without_tags_only', default=None,
            help=('Push only strings that do not contain specific tags'),
        )
        parser.add_argument(
            '--dry-run', action='store_true',
            dest='dry_run', default=False,
            help=('Do not push to CDS'),
        )
        parser.add_argument(
            '--no-wait', action='store_true', dest='no_wait', default=False,
            help=('Disable polling for upload results'),
        )
        parser.add_argument(
            '--override-tags', action='store_true', dest='override_tags', default=False,
            help=('Override tags when pushing content'),
        )
        parser.add_argument(
            '--override-occurrences', action='store_true', dest='override_occurrences', default=False,
            help=('Override occurrences when pushing content'),
        )
        parser.add_argument(
            '--do-not-keep-translations', action='store_true', dest='do_not_keep_translations', default=False,
            help=('Remove translations when source strings change'),
        )
        parser.add_argument(
            '--verbose', '-v', action='store_true',
            dest='verbose_output', default=False,
            help=('Verbose output'),
        )
        parser.add_argument(
            '--symlinks', '-s', action='store_true', dest='symlinks',
            default=False,
            help=('Follows symlinks to directories when examining source code '
                  'and templates for translation strings.'),
        )
        parser.add_argument(
            '--key-generator', dest='key_generator', default='source',
            choices=['source', 'hash'],
            help=('Use "hash" or "source" based keys (default: source)'),
        )

    def handle(self, *args, **options):
        self.verbose_output = options['verbose_output']
        self.domain = options['domain']
        self.ignore_patterns = []
        self.purge = options['purge']
        self.symlinks = options['symlinks']
        self.append_tags = options['append_tags']
        self.with_tags_only = options['with_tags_only']
        self.without_tags_only = options['without_tags_only']
        self.dry_run = options['dry_run']
        self.override_tags = options['override_tags']
        self.override_occurrences = options['override_occurrences']
        self.do_not_keep_translations = options['do_not_keep_translations']
        self.no_wait = options['no_wait']
        self.key_generator = options['key_generator']
        extensions = options['extensions']
        if self.domain == 'djangojs':
            exts = extensions if extensions else ['js']
        else:
            exts = extensions if extensions else ['html', 'txt', 'py']
        self.extensions = handle_extensions(exts)
        self.locale_paths = []
        self.default_locale_path = None

        self.string_collection = SourceStringCollection()

        # Create an extractor for Python files, to reuse for all files
        self.python_extractor = Extractor()
        # Support `t()` and `ut()` calls made on the Django module.
        self.python_extractor.register_functions(
            'transifex.native.django.t',
            'transifex.native.django.ut',
            'transifex.native.django.lazyt')

        self.stats = {'processed_files': 0, 'strings': []}

        # Search all related files and collect translatable strings,
        # storing them in `self.string_collection`
        self.collect_strings()

        # Push the strings to the CDS
        if not self.dry_run:
            self.push_strings()

    def collect_strings(self):
        """Search all related files, collect and store translatable strings.

        Stores found strings in `self.string_collection`.
        """
        Color.echo(
            '[high]\n'
            '##############################################################\n'
            'Transifex Native: Parsing files to detect translatable content'
            '[end]'
        )
        files = self._find_files('.', 'push')
        for f in files:
            extracted_strings = self._extract_strings(f)
            self.string_collection.extend(extracted_strings)
            self.stats['processed_files'] += 1
            if extracted_strings and len(extracted_strings):
                self.stats['strings'].append((f.file, len(extracted_strings)))

        # Append optional CLI tags
        if self.append_tags:
            extra_tags = [x.strip() for x in self.append_tags.split(',')]
            for key, string in self.string_collection.strings.items():
                # Append tags in SourceString
                string.tags = extra_tags

        # Filter out strings based on tags, i.e. only push strings
        # that contain certain tags or do not contain certain tags
        if self.with_tags_only:
            included_tags = {x.strip() for x in self.with_tags_only.split(',')}
        else:
            included_tags = set()
        if self.without_tags_only:
            excluded_tags = {x.strip()
                             for x in self.without_tags_only.split(',')}
        else:
            excluded_tags = set()

        if included_tags or excluded_tags:
            self.string_collection.update(
                [
                    string
                    for key, string in self.string_collection.strings.items()
                    if included_tags.issubset(set(string.tags))
                    and not excluded_tags.intersection(set(string.tags))
                ]
            )
        self._show_collect_results()

    def push_strings(self):
        """Push strings to the CDS."""
        total = len(self.string_collection.strings)
        if total == 0:
            Color.echo('[warn]There are no strings to push to Transifex.[end]')
            return

        Color.echo(
            'Pushing [warn]{}[end] unique translatable strings '
            'to Transifex...'.format(total)
        )
        status_code, response_content = tx.push_source_strings(
            self.string_collection.strings.values(), self.purge,
            self.do_not_keep_translations, self.override_tags,
            self.override_occurrences
        )

        if self.no_wait:
            Color.echo('Queued')
            return

        job_url = response_content['data']['links']['job']
        status = 'starting'
        while status in ['starting', 'pending', 'processing']:
            time.sleep(1)
            status_code, response_content = tx.get_push_status(job_url)
            new_status = response_content['data']['status']
            if new_status != status:
                status = new_status
                if status == 'pending':
                    sys.stdout.write('In queue...')
                elif status == 'processing':
                    sys.stdout.write('Processing...')
            else:
                sys.stdout.write('.')
            sys.stdout.flush()

        Color.echo('')
        self._show_push_results(status_code, response_content)

    def _extract_strings(self, translatable_file):
        """Extract source strings from the given file.

        Supports both Python files and Django template files.

        :param TranslatableFile translatable_file: the file to search
        :return: a list of SourceString objects
        :rtype: list
        """
        fkeygen = generate_key
        if self.key_generator == 'hash':
            fkeygen = generate_hashed_key

        self.verbose('Processing file %s in %s' % (
            translatable_file.file, translatable_file.dirpath
        ))
        encoding = (
            settings.FILE_CHARSET if (
                hasattr(settings, 'FILE_CHARSET')
                and self.settings_available
            )
            else 'utf-8'
        )
        try:
            src_data = self._read_file(translatable_file.path, encoding)
        except UnicodeDecodeError as e:
            self.verbose(
                'UnicodeDecodeError: skipped file %s in %s (reason: %s)' % (
                    translatable_file.file, translatable_file.dirpath, e,
                )
            )
            return None

        _, extension = os.path.splitext(translatable_file.file)
        # Python file
        if extension == '.py':
            return self.python_extractor.extract_strings(
                force_text(src_data),
                translatable_file.path[2:],
                fkeygen
            )

        # Template file
        return extract_transifex_template_strings(
            src_data,
            translatable_file.path[2:],
            encoding,
            fkeygen
        )

    def _show_collect_results(self):
        """Display results of collecting source strings from files."""
        total_strings = sum([x[1] for x in self.stats['strings']])
        Color.echo(
            'Processed [warn]{}[end] files and found [warn]{}[end] '
            'translatable strings in [warn]{}[end] of them.'.format(
                self.stats['processed_files'], total_strings, len(self.stats)
            )
        )
        if self.verbose_output:
            file_list = '\n'.join(
                [
                    u'[pink]{}.[end] {}'.format((cnt + 1), string_repr(x))
                    for cnt, x in enumerate(
                        self.string_collection.strings.values()
                    )
                ]
            )
            Color.echo(file_list)

    def _show_push_results(self, status_code, response_content):
        """Display results of pushing the source strings to CDS.

        :param int status_code: the HTTP status code
        :param dict response_content: the content of the response
        """
        try:
            data = response_content.get('data')
            status = data.get('status')
            errors = data.get('errors', [])
            if status == 'completed':
                details = data.get('details')
                created = details.get('created')
                updated = details.get('updated')
                skipped = details.get('skipped')
                deleted = details.get('deleted')
                failed = details.get('failed')
                Color.echo(
                    '[green]\nSuccessfully pushed strings to Transifex.[end]'
                )

                if created > 0:
                    Color.echo(
                        '[high]Created strings:[end] '
                        '[warn]{created}[end]'.format(created=created))

                if updated > 0:
                    Color.echo(
                        '[high]Updated strings:[end] '
                        '[warn]{updated}[end]'.format(updated=updated))

                if skipped > 0:
                    Color.echo(
                        '[high]Skipped strings:[end] '
                        '[warn]{skipped}[end]'.format(skipped=skipped))

                if deleted > 0:
                    Color.echo(
                        '[high]Deleted strings:[end] '
                        '[warn]{deleted}[end]'.format(deleted=deleted))

                if failed > 0:
                    Color.echo(
                        '[high]Failed strings:[end] '
                        '[warn]{failed}[end]'.format(failed=failed))
            else:
                Color.echo(
                    '[error]\nCould not push strings to Transifex.[end]')

            if len(errors) > 0:
                Color.echo(
                    '[high]Errors:[end] {errors}[end]\n'.format(
                        errors='\n'.join(errors)
                    )
                )
        except Exception:
            self.output(
                '(Error while printing formatted report, '
                'falling back to raw format)\n'
                'Status: {code}\n'
                'Content: {content}'.format(
                    code=status_code,
                    content=response_content,
                )
            )


def string_repr(source_string):
    """Return a nice visual representation of the given
    SourceString and all its properties.

    Any property that isn't populated (e.g. tags
    or developer comment) will be omitted.
    """
    return (
        '[green]"{string}"[end]\n'
        '{key}'
        '{context}'
        '{comment}'
        '{charlimit}'
        '{tags}'
        '   [high]occurrences:[end] [file]{occurrences}[end]\n'
    ).format(
        string=source_string.string,
        key=(
            '   [high]key:[end] "[yel]{}[end]"\n'.format(
                source_string.key
            )
        ),
        context=(
            '   [high]context:[end] {}\n'.format(
                u', '.join(source_string.context)
            )
            if source_string.context else ''
        ),
        comment=(
            '   [high]comment:[end] {}\n'.format(
                source_string.developer_comment
            )
            if source_string.developer_comment else ''
        ),
        charlimit=(
            '   [high]character limit:[end] {}\n'.format(
                source_string.character_limit
            )
            if source_string.character_limit else ''
        ),
        tags=(
            '   [high]tags:[end] {}\n'.format(
                u', '.join(source_string.tags)
            )
            if source_string.tags else ''
        ),
        occurrences=u', '.join(source_string.occurrences),
    )
