from PyQt5.Qsci import *

__all__ = ['get_lexer_by_ext', 'set_lexer_by_menu']

LEXERS = {

    ('Bash', QsciLexerBash): ('sh', 'ksh', 'bash', 'ebuild', 'eclass', 'exheres-0', 'exlib'),
    ('C', QsciLexerCPP): ('cpp', 'hpp', 'c++', 'h++', 'cc', 'hh', 'cxx', 'hxx', 'C', 'H', 'cp', 'CPP'),
    ('C++', QsciLexerCPP): ('cpp', 'hpp', 'c++', 'h++', 'cc', 'hh', 'cxx', 'hxx', 'C', 'H', 'cp', 'CPP'),
    ('C#', QsciLexerCSharp): ('cs'),
    ('CSS', QsciLexerCSS): ('css'),
    ('HTML', QsciLexerHTML): ('html', 'htm', 'xhtml', 'xslt'),
    ('Java', QsciLexerJava): ('java'),
    ('Perl', QsciLexerPerl): ('pl', 'pm', 't'),
    ('Python', QsciLexerPython): ('py', 'pyw', 'sc', 'tac', 'sage'),
    ('SQL', QsciLexerSQL): ('sql'),
    ('TeX', QsciLexerTeX): ('tex', 'aux', 'toc'),
    ('XML', QsciLexerXML): ('xml', 'xsl', 'rss', 'xslt', 'xsd', 'wsdl', 'wsf'),

}


def get_lexer_by_ext(file):
    """Function return lexer according file extension"""
    file_name, file_ext = file.split('.')
    for key, value in LEXERS.items():
        if file_ext in value:
            lexer = key[1]

            return lexer


def set_lexer_by_menu(item):
    """Function return lexer according menu item"""
    for key, value in LEXERS.items():
        if item in key[0]:
            lexer = key[1]

            return lexer

def testing():
    """Function for testing"""
    print(get_lexer_by_ext('file.py'))
    print(set_lexer_by_menu('Python'))


if __name__ == '__main__':
    testing()

