import sys
from antlr4 import *
from lexanalyz.gen.LexerGo import LexerGo
from lexanalyz.gen.ParserGo import ParserGo
from lexanalyz.gen import ParserGoListener


class ParserGoListener(ParserGoListener):
    def enterHi(self, ctx):
        print("Hello: %s" % ctx.ID())
    def main(argv):
        lexer = LexerGo(StdinStream())
        stream = CommonTokenStream(lexer)
        parser = ParserGo(stream)
        tree = parser.hi()
        printer = ParserGoListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
if __name__ == '__main__':
    main(sys.argv)