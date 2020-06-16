from library.antlr_ast import ast


def generatedAst(text):

    ParseTree = ast.parse(text, start="sourceFile")

    old_tree = ast.process_tree(ParseTree)

    return old_tree

