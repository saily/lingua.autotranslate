# -*- coding: utf-8 -*-
import argparse
import polib
import re
import time

from translate import Translator


DEFAULT = re.compile(r'Default:\s(.*)')
SOURCE_LANGUAGE = 'en'
BREATHE = 0.25


def log(bash_color, type, text):
    print u'[\033[{0}m {1} \033[0m] {2}'.format(bash_color, type, text)


def autotranslate(path, target_language, ignore_already_translated=True):
    """Given a po file which is opened using polib and processed through
       Google Translator for all untranslated items by default
    """

    try:
        catalog = polib.pofile(path)
    except UnicodeDecodeError:
        raise Exception(("Encoding problem while parsing {0}, are you "
                         "sure that's a PO file?").format(path))

    translator = Translator(to_lang='de', from_lang=SOURCE_LANGUAGE)
    try:
        for idx, entry in enumerate(catalog):

            if ignore_already_translated and entry.translated():
                continue

            default_text = DEFAULT.match(entry.comment)
            if default_text:
                to_translate = default_text.group(1)
            else:
                to_translate = entry.msgid

            try:
                translated = translator.translate(to_translate)
            except:
                log(31, 'Error', entry.msgid)
                continue

            log(32, 'Success', u'{0} -> {1}'.format(to_translate, translated))

            # Save entry
            catalog[idx].msgstr = translated
            time.sleep(BREATHE)

    except KeyboardInterrupt:
        pass

    catalog.save()


def AutoTranslator():
    parser = argparse.ArgumentParser(description='Translate Po files.')
    parser.add_argument('-i', dest='input', action='append', nargs=2,
                              required=True, metavar=('<locale>', '<po file>'),
                              help='Locale and filename of po-file to process')
    parser.add_argument('--force', default=False, required=False,
                                   help='Force retranslation of all translated'
                                        'msgids.')
    options = parser.parse_args()

    for locale, pofile in options.input:
        autotranslate(pofile, locale)