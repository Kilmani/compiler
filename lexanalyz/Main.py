
from lexanalyz.GenAst import generatedAst

from lexanalyz.GeneratedIR import tokenGen, GeneratedIR


def readFile(filename):
   file = open(filename, 'r')
   goCode = file.read()
   return goCode

def main():

   golangCode = readFile("test.go")    # Read golang



   ast = generatedAst(golangCode)      # build parse tree and build ast

   print("AST: ")
   print(ast)

   irCode = tokenGen(str(ast))

   print(irCode)




if __name__ == '__main__':
   main()