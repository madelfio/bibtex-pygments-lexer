### BibTeX support for pygments

Enables [BibTeX][1] syntax highlighting for [Pygments][2].  Pygments is a
Python-based syntax highlighter with built-in support for many file formats,
but there was no existing lexer for BibTeX.  Many popular projects use 
Pygments (such as [Pandoc][3], [Jekyll][4], and [Pelican][5]), and can use
this lexer for pages containing BibTeX.

#### Installation

The lexer should be installed into the Python environment that contains the
Pygments package.

To install from the Python Package Index:

    $ pip install bibtex-pygments-lexer

Or, to install straight from source:

    $ python setup.py install

#### Development

    $ vim bibtex-lexer/__init__.py
    $ python setup.py install
    $ pygmentize input_file.bib

[1]: http://www.bibtex.org/
[2]: http://pygments.org/
[3]: http://johnmacfarlane.net/pandoc/
[4]: http://jekyllrb.com/
[5]: http://docs.getpelican.com/
