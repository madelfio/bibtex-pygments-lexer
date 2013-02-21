import sys
import os
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='BibTeX Pygments Lexer',
    version='0.0.1',
    description='Pygments Lexer for BibTeX',
    author='Marco D. Adelfio',
    packages=['bibtex_lexer'],
    entry_points='''[pygments.lexers]
bibtexlexer = bibtex_lexer:BibtexLexer
'''
)
