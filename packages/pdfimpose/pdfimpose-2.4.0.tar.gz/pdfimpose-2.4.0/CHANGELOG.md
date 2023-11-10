* pdfimpose 2.4.0 (2023-11-09)

    * Add Python3.12 support.
    * Drop Python3.9 support.
    * Rename xdg dependency to xdg-base-dirs (project was renamed).
    * Fix bug: pdfimpose could not read PDF file from standard input.
    * Fix bug: PDF files with rotated pages are handled correctly (closes #38).

    -- Louis Paternault <spalax@gresille.org>

* pdfimpose 2.3.0 (2022-11-07)

    * Python3.11 support.

    -- Louis Paternault <spalax@gresille.org>

* pdfimpose 2.2.1 (2022-08-18)

    * [cutstackfold] Fix a bug with option --group : some source pages could be lost.
    * Minor refactoring and code improvement.

    -- Louis Paternault <spalax@gresille.org>

* pdfimpose 2.2.0 (2022-08-17)

    * [cards] Add a --back option.
    * [cutstackfold, copycutfold, perfect, saddle] Add a --group option (see #33).
    * Add a warning on --creep option: it is broken. See #36.

    -- Louis Paternault <spalax@gresille.org>

* pdfimpose 2.1.1 (2022-03-21)

    * PyMuPDF dependency
        * Fix minimum PyMuPDF version.
        * Fix compatibility issue with PyMuPDF>1.19.
    * [saddle, perfect] A 2 nanometers overlap is allowed between pages (was 0.2 nanometers before).
    * Documentation
        * Fix formatting of `--help` text (closes #34).
        * Improve documentation about creep (closes #35).
        * Improve documentation about signatures (closes #32).

    -- Louis Paternault <spalax@gresille.org>

* pdfimpose 2.1.0 (2022-02-15)

    * [setup] Fix version of a dependency.
    * Python3.10 support.
    * Remove cryptic debug message.

    -- Louis Paternault <spalax@gresille.org>

* pdfimpose 2.0.1 (2021-08-04)

    * Drop python3.8 support (this was already the case in version 2.0.0, but was (wrongly) documented otherwise).

    -- Louis Paternault <spalax@gresille.org>

* pdfimpose 2.0.0 (2021-08-04)

    Warning: This version is backward-incompatible with pdfimpose version 1.

    * pdfimpose has been fully rewritten
      * It now support several imposition schemas: cards, copycutfold, cutstackfold, onepagezine, perfect, saddle, wire (closes #14 #18 #25).
      * It now support margins and fold creep (closes #19 #21).
      * It now support crop and bind marks (closes #20).
      * Options can be set in a configuration file (closes #22).
    * Python support
      * Drop python2, python3.5 to python3.7 support.
      * Add python3.8 to python3.9 support.
    * Minor improvements to setup.
    * Licence changed from GPL to AGPL, due to a new PDF backend used (pyMuPDF), itself licenced under AGPL (closes #29).

    -- Louis Paternault <spalax@gresille.org>

* pdfimpose 1.1.0 (2019-02-12)

    * Python support

      * Add python3.7 support.
      * Drop python3.4 support.

    * Features and Bugs

      * Fix an orientation error with option --sheets.
      * Fix a bug in `--paper` option, which, with ``--paper=A3``, would make a A5 paper be imposed on A4 paper instead of A3 paper (closes #16).

    * Minor improvements to:

      * documentation;
      * setup;
      * continuous integration;
      * examples.

    -- Louis Paternault <spalax@gresille.org>

* pdfimpose 1.0.0 (2017-12-28)

    * Add python3.6 support.
    * Several files can be given in argument. They are concatenated, then imposed (closes #10).
    * No longer crash when using pdfimpose on file without any metadata (closes #12).
    * Warn user if all pages do not have the same dimension (closes #11).
    * Display nicer messages with several input-file related errors (absent, unreadable, malformed, etc. file).
    * Add options `--paper` and `--sheets`, to define how document is folded more easily (closes #7).
    * Horizontal and vertical folds are alternated as much as possible (closes #8).

    -- Louis Paternault <spalax@gresille.org>

* pdfimpose 0.1.1 (2015-06-13)

    * Python3.5 support
    * Several minor improvements to setup, test and documentation.
    * [doc] Wrote missing parts

    -- Louis Paternault <spalax@gresille.org>

* pdfimpose 0.1.0 (2015-04-15)

    * Initial release.

    -- Louis Paternault <spalax@gresille.org>
