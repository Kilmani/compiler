import sys
from antlr4 import *
from lexanalyz.gen import LexerGo
from lexanalyz.gen import LexerGo
from lexanalyz.gen import ParserGo
from lexanalyz.gen import ParserGoListener



def main(argv):
    file = open('test.go', 'r')
    input_stream = FileStream(argv[1])
    lexer = LexerGo(file)
    stream = CommonTokenStream(lexer)
    parser = ParserGo(stream)
    tree = parser.startRule()

    class ParserGoListener(ParseTreeListener):
        def enterKey(self, ctx):
            pass

        def exitKey(self, ctx):
            pass

        def enterValue(self, ctx):
            pass

        def exitValue(self, ctx):
            pass

    class KeyPrinter(ParserGoListener):
        def exitKey(self, ctx):
            print("Oh, a key!")
            tree = parser.startRule()
    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

