import sys
import antlr4
from antlr4 import *
from lexanalyz.gen.LexerGo import *
from lexanalyz.gen.ParserGo import *
from lexanalyz.gen.ParserGoListener import ParserGoListener
from lexanalyz.gen.ParserGoVisitor import ParserGoVisitor

from antlr4.tree.Trees import Trees

import llvmlite.binding as llvm
from lexanalyz.codeGen import CodeGen
import symtable


def optimize(module_ref):
   pass_manager_builder = llvm.create_pass_manager_builder()

   module_pass_manager = llvm.create_module_pass_manager()

   # Optimize the fuck out of this
   module_pass_manager.add_constant_merge_pass()
   module_pass_manager.add_dead_arg_elimination_pass()
   module_pass_manager.add_function_attrs_pass()
   module_pass_manager.add_function_inlining_pass(5)
   module_pass_manager.add_global_dce_pass()
   module_pass_manager.add_global_optimizer_pass()
   module_pass_manager.add_ipsccp_pass()
   module_pass_manager.add_dead_code_elimination_pass()
   module_pass_manager.add_cfg_simplification_pass()
   module_pass_manager.add_gvn_pass()
   module_pass_manager.add_instruction_combining_pass()
   module_pass_manager.add_licm_pass()
   module_pass_manager.add_sccp_pass()
   module_pass_manager.add_sroa_pass()
   module_pass_manager.add_type_based_alias_analysis_pass()
   module_pass_manager.add_basic_alias_analysis_pass()

   pass_manager_builder.populate(module_pass_manager)

   module_pass_manager.run(module_ref)

def generate_object_file(module):
   llvm.initialize()
   llvm.initialize_native_target()
   llvm.initialize_native_asmprinter()
   target = llvm.Target.from_default_triple()

   target_machine = target.create_target_machine(opt=3)
   module_ref = llvm.parse_assembly(str(module))

   optimize(module_ref)

   obj = target_machine.emit_object(module_ref)

   with open("./out/program.o", "wb") as f:
      f.write(obj)


def main():
   f = open('test.go', 'r')
   TestCode = f.read()
   print('***************'+'\n'+TestCode+'\n'+'***************'+'\n')
   lexer = LexerGo(antlr4.InputStream(TestCode))
   stream = CommonTokenStream(lexer)
   parser = ParserGo(stream)
   tree = parser.sourceFile()
   printer = ParserGoListener()
   walker = ParseTreeWalker()
   walker.walk(printer, tree)
   # print("ЛИСТЕНЕР "+walker.walk(printer, tree))
   visitor = ParserGoVisitor()
   result = ParserGoVisitor.visit(visitor, tree)
   # print("ВИЗИТОР "+result)
   # print(tree.toStringTree())
   print(Trees.toStringTree(tree, None, parser))

   print(printer.module)
   generate_object_file(printer.module)

   codegen = CodeGen()

   module = codegen.module
   builder = codegen.builder
   printf = codegen.printf

   codegen.create_ir()
   codegen.save_ir("output.ll")
   
if __name__ == '__main__':
   main()