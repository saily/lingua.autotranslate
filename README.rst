Introduction
============

lingua.autotranslate is an autotranslation toolkit for .po files using Google
Translate API.

Usage
-----

To use this package you should add the following line to your eggs buildout
section::

    eggs =
        lingua.autotranslate

When running ``bin/buildout`` it will create a new console script for you,
``bin/autotranslate`` which requires at least two parameters::

    ~/workspace/my.product $ bin/autotranslate -h
    usage: autotranslate [-h] -i <locale> <po file> [-u]

    Translate Po files.

    optional arguments:
      -h, --help            show this help message and exit
      -i <locale> <po file>
                            Locale and filename of po-file to process
      -u                    Force updating translations by retranslating all
                            msgids.

Example:
--------

See translation example below.::

    ~/workspace/my.product $ bin/autotranslate -i de src/my/product/locales/de/LC_MESSAGES/my.product.po
    [ Success ] New product -> Neues Produkt
    [ Success ] Specification -> Beschreibung
    [ Success ] Language -> Sprache
    ...


Author
------

- Daniel Widerin  <daniel@widerin.net>

