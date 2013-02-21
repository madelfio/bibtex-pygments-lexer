# Based on spec summary at
# http://artis.imag.fr/~Xavier.Decoret/resources/xdkbibtex/bibtex_summary.html

from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import Text, Comment, Keyword, String, Number, Other, \
        Punctuation, Literal, Name

class BibtexLexer(RegexLexer):
    name = 'BibTeX'
    aliases = ['bibtex', 'bib']
    filenames = ['*.bib']

    tokens = {

        'whitespace': [
            (r'\s+', Text)
        ],

        'bracket': [
            (r'[^}{]+', Literal.String.Double),
            (r'{', Punctuation, '#push'),
            (r'}', Punctuation, '#pop'),
        ],

        'value': [
            include('whitespace'),
            (r'-?(0|[1-9]\d*)', Number.Integer),
            (r'"(\\\\|\\"|[^"])*"', Literal.String.Double),
            (r"'(\\\\|\\'|[^'])*'", Literal.String.Single),
            (r'{', Punctuation, 'bracket'),
            (r'[^,}{]+', Text),
        ],

        'root': [
            include('whitespace'),
            (r'(?i)(@(?:string|preamble))(\s*)({)',
             bygroups(Keyword.Declaration, Text, Punctuation),
             'single_attribute'),
            (r'(?i)(@(?:article|book|booklet|conference|inbook|incollection|'
             r'inproceedings|manual|mastersthesis|misc|phdthesis|proceedings|'
             r'techreport|unpublished))(\s*)({)',
             bygroups(Keyword.Declaration, Text, Punctuation), 'entry'),
            (r'(@[^ {]*)(\s*)({)',
             bygroups(Keyword, Text, Punctuation), 'entry'),
            (r'.*\n', Comment)
        ],

        'entry': [
            include('whitespace'),
            (r'([^, ]*)(\s*)(\,)',
             bygroups(Name.Label, Text, Punctuation), 'multi_attributes'),
        ],

        'multi_attributes': [
            include('whitespace'),
            (r'}', Punctuation, '#pop:2'), # pop back to root
            (r'([^}=\s]*)(\s*=)', bygroups(Name.Attribute, Text), 'multi_value'),
            (r'[^}]+\n', Text),
        ],

        'multi_value': [
            include('value'),
            (r',', Punctuation, '#pop'), # pop back to multi_attributes
            (r'}', Punctuation, '#pop:3'), # pop back to root
        ],

        'single_attribute': [
            include('whitespace'),
            (r'}', Punctuation, '#pop'), # pop back to root
            (r'([^}=\s]*)(\s*=)', bygroups(Name.Label, Text), 'single_value'),
            (r'[^}]+\n', Text),
        ],

        'single_value': [
            include('value'),
            (r'}', Punctuation, '#pop:2'), # pop back to root
        ],

    }
