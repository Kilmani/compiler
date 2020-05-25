import sys
import antlr4
from antlr4 import *
from lexanalyz.gen.LexerGo import *
from lexanalyz.gen.ParserGo import *
from lexanalyz.gen.ParserGoListener import ParserGoListener
from lexanalyz.gen.ParserGoVisitor import ParserGoVisitor

from antlr4.tree.Trees import Trees

import symtable

import llvmlite
from llvmlite import ir
def main():

    f = open('test.go', 'r')
    TestCode = f.read()
    inputCode = antlr4.InputStream(TestCode)
    lexer = LexerGo(inputCode)
    stream = CommonTokenStream(lexer)
    parser = ParserGo(stream)
    tree = parser.eos()
    print(tree.toStringTree())

    symtable.symtable()



if __name__ == '__main__':
    main()