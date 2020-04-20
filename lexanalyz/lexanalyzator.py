import sys
from antlr4 import *
from lexanalyz.gen.LexerGo import LexerGo
from lexanalyz.gen.ParserGo import ParserGo
#from lexanalyz.gen import ParserGoListener

def main(argv):
    input_stream = FileStream(argv[0])
    lexer = LexerGo(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ParserGo(stream)
    tree = parser.Parse

    print(tree)
if __name__ == '__main__':
    main(sys.argv)
