
from PyQt5.QtGui import *
from PyQt5.Qsci import *

FONT_FAMILY = "Courier"
BACKGROUND_COLOR = '#f8f8f8'
FOREGROUND_COLOR = '#535353'
MARGIN_BACKGROUND = "#2b2b2b" # "#313335"
MARGIN_FOREGROUND = "#676a6d"
FOLD_MARGIN_BACKGROUND = "#2b2b2b" # "#313335"
EDGE_COLOR = "#BBB8B5"
SEL_BACKGROUND = "#535353" # "#606060"
SEL_FOREGROUND = "#222222"
IND_BACKGROUND = "#676a6d"
IND_FOREGROUND = "#676a6d"
MARKER_BACKGROUND = "#2b2b2b" # "#313335"
MARKER_FOREGROUND = "#676a6d"


use_indentation_markers = True



class Editor(QsciScintilla):
    ARROW_MARKER_NUM = 8
    def __init__(self, parent=None):
        super(Editor, self).__init__(parent)
        self.bgcolor = '#535353'


        global use_indentation_markers

        # FONT
        # Set the default font
        font = QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.setFont(font)
        self.setMarginsFont(font)

        # DEFAULT BACKGROUND AND FOREGROUND
        self.setPaper(QColor(BACKGROUND_COLOR))
        self.setColor(QColor(FOREGROUND_COLOR))

        # MARGIN LINE NUMBERS
        fontmetrics = QFontMetrics(font)
        self.setMarginsFont(font)
        self.setMarginWidth(0, fontmetrics.width("00000") + 6)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("#cccccc"))

        # MARGIN BACKGROUND AND FOREGROUND
        self.setMarginsBackgroundColor(QColor(MARGIN_BACKGROUND))
        self.setMarginsForegroundColor(QColor(MARGIN_FOREGROUND))

        self.setMarginSensitivity(1, True)
        #        self.connect(self,
        #            SIGNAL('marginClicked(int, int, Qt::KeyboardModifiers)'),
        #            self.on_margin_clicked)
        self.markerDefine(QsciScintilla.RightArrow,
                          self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ee1111"),
                                      self.ARROW_MARKER_NUM)

        # BRACE MATCHING
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        # CURRENT LINE
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor("#ffe4e4"))
        self.setCaretForegroundColor(QColor("#535353"))
        # SELECTION BACKGROUND AND FOREGROUND
        self.setSelectionBackgroundColor(QColor(SEL_BACKGROUND))
        self.setSelectionForegroundColor(QColor(SEL_FOREGROUND))

        # TABS

        self.setIndentationsUseTabs(True)
        self.setIndentationWidth(4)
        self.setTabIndents(True)
        self.setAutoIndent(True)
        self.setBackspaceUnindents(True)
        self.setTabWidth(4)

        # indentation guides
        self.setIndentationGuides(use_indentation_markers)
        # TABS BACKGROUND AND FOREGROUND
        self.setIndentationGuidesBackgroundColor(QColor(IND_BACKGROUND))
        self.setIndentationGuidesForegroundColor(QColor(IND_FOREGROUND))


        # FOLDING MARGIN
        self.setFolding(QsciScintilla.PlainFoldStyle)
        self.setMarginWidth(2, 10) # (2,14)
        # FOLDING MARKERS
        self.markerDefine("V", QsciScintilla.SC_MARKNUM_FOLDEROPEN)
        self.markerDefine(">", QsciScintilla.SC_MARKNUM_FOLDER)
        self.markerDefine("V", QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        self.markerDefine(">", QsciScintilla.SC_MARKNUM_FOLDEREND)
        # FOLDING MARKERS BACKGROUND AND FOREGROUND
        self.setMarkerBackgroundColor(QColor(MARKER_BACKGROUND))
        self.setMarkerForegroundColor(QColor(MARGIN_FOREGROUND))
        self.setFoldMarginColors(QColor(FOLD_MARGIN_BACKGROUND), QColor(FOLD_MARGIN_BACKGROUND))

        # FOLDING LINE DISABLE
        self.SendScintilla(QsciScintilla.SCI_SETFOLDFLAGS, 0)

        # AUTO COMPLETION
        self.setAutoCompletionSource(QsciScintilla.AcsDocument)
        self.setAutoCompletionThreshold(2)

        # DISABLE HORIZONTAL SCROLLBAR
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)

        self.setStyleSheet("""
        QsciScintilla
        {
             border: 0px solid black;
             padding: 0px;
             border-radius: 0px;
             opacity: 100;
             font-size: 10px !important;
        }
        """)
        text = bytearray(str.encode("Arial"))

        self.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, text)
    def on_margin_clicked(self, nmargin, nline, modifiers):
        # Toggle marker for the line the margin was clicked on
        if self.markersAtLine(nline) != 0:
            self.markerDelete(nline, self.ARROW_MARKER_NUM)
        else:
            self.markerAdd(nline, self.ARROW_MARKER_NUM)
    def setLexer(self, lexer=None):
        super(Editor, self).setLexer(lexer)

        self.font2 = QFont()
        self.font2.setFamily(FONT_FAMILY)
        self.font2.setFixedPitch(True)
        self.font2.setPointSize(10)

        lexer.setFont(self.font2)

        # lexer.setColor(QColor(FOREGROUND_COLOR))
        lexer.setPaper(QColor(BACKGROUND_COLOR))

        #TODO: Remove this temporary solution for highlighting
        try:
            lexer.setColor(QColor("#8757ad"), lexer.ClassName)
        except:
            pass
        try:
            lexer.setColor(QColor("#446fbd"), lexer.Keyword)
        except:
            pass
        try:
            lexer.setColor(QColor("#949494"), lexer.Comment)
        except:
            pass
        try:
            lexer.setColor(QColor("#6d8600"), lexer.Number)
        except:
            pass
        try:
            lexer.setColor(QColor("#e88501"), lexer.DoubleQuotedString)
        except:
            pass
        try:
            lexer.setColor(QColor("#e88501"), lexer.TripleSingleQuotedString)
        except:
            pass
        try:
            lexer.setColor(QColor("#e88501"), lexer.TripleDoubleQuotedString)
        except:
            pass
        try:
            lexer.setColor(QColor("#e88501"), lexer.DoubleQuotedString)
        except:
            pass
        try:
            lexer.setColor(QColor("#8757ad"), lexer.FunctionMethodName)
        except:
            pass
        try:
            lexer.setColor(QColor("#535353"), lexer.Operator)
        except:
            pass
        try:
            lexer.setColor(QColor("#292929"), lexer.Identifier)
        except:
            pass
        try:
            lexer.setColor(QColor("#949494"), lexer.CommentBlock)
        except:
            pass
        try:
            lexer.setColor(QColor("#e88501"), lexer.UnclosedString)
        except:
            pass
        try:
            lexer.setColor(QColor("#797979"), lexer.HighlightedIdentifier)
        except:
            pass
        try:
            lexer.setColor(QColor("#535353"), lexer.Decorator)
        except:
            pass

def main():
    """For standalone starting Editor in Python mode"""
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    editor = Editor()
    editor.resize(640, 500)
    editor.setCaretLineBackgroundColor(QColor("#535353"))
    editor.setCaretForegroundColor(QColor("#535353"))

    font = QFont()
    font.setFamily(FONT_FAMILY)
    font.setFixedPitch(True)
    font.setPointSize(10)
    lexer = QsciLexerPython()
    lexer.setDefaultFont(font)
    lexer.setColor(QColor("#292929"))

    editor.setLexer(lexer)

    # high light code
    lexer.setColor(QColor("#292929"))
    lexer.setPaper(QColor("#333333"))
    lexer.setColor(QColor("#8757ad"), QsciLexerPython.ClassName)
    lexer.setColor(QColor("#446fbd"), QsciLexerPython.Keyword)
    lexer.setColor(QColor("#949494"), QsciLexerPython.Comment)
    lexer.setColor(QColor("#6d8600"), QsciLexerPython.Number)
    lexer.setColor(QColor("#e88501"), QsciLexerPython.DoubleQuotedString)
    lexer.setColor(QColor("#e88501"), QsciLexerPython.TripleSingleQuotedString)
    lexer.setColor(QColor("#e88501"), QsciLexerPython.TripleDoubleQuotedString)
    lexer.setColor(QColor("#e88501"), QsciLexerPython.DoubleQuotedString)
    lexer.setColor(QColor("#8757ad"), QsciLexerPython.FunctionMethodName)
    lexer.setColor(QColor("#535353"), QsciLexerPython.Operator)
    lexer.setColor(QColor("#292929"), QsciLexerPython.Identifier)
    lexer.setColor(QColor("#949494"), QsciLexerPython.CommentBlock)
    lexer.setColor(QColor("#e88501"), QsciLexerPython.UnclosedString)
    lexer.setColor(QColor("#797979"), QsciLexerPython.HighlightedIdentifier)
    lexer.setColor(QColor("#535353"), QsciLexerPython.Decorator)


    editor.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
