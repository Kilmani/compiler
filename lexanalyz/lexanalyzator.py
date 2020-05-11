import sys
from antlr4 import *
from lexanalyz.gen.LexerGo import LexerGo
from lexanalyz.gen.ParserGo import ParserGo
from lexanalyz.gen.ParserGoListener import ParserGoListener


class ParserGoListenerPrint(ParserGoListener):
   def enterHi(self, ctx):
      print("Hello: %s" % ctx.ID())

def main():
   f = open('test.go', 'r')
   giveMeInput = f.read()
   print("PRINT: ".format(giveMeInput))

   i_stream = InputStream(giveMeInput)

   lexer = LexerGo(i_stream)
   t_stream = CommonTokenStream(lexer)
   parser = ParserGo(t_stream)
   tree = parser.element()
   printer = ParserGoListenerPrint()
   walker = ParseTreeWalker()
   walker.walk(printer, tree)

if __name__ == '__main__':
   main()