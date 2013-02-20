###BibTeX support for pygments

I wanted to be able to highlight [BibTeX][1] files using [pygments][2].

Based loosely on the [puppet-pygments-lexer][3].

#### Installation

    $ pip install bibtex-pygments-parser

Or, to install straight from source:

    $ python setup.py install

#### Development

    $ vim bibtex-lexer/__init__.py
    $ python setup.py install
    $ pygmentize input_file.bib

[1]: http://www.bibtex.org
[2]: http://pygments.org
[3]: https://github.com/rodjek/puppet-pygments-lexer/
