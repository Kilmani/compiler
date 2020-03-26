# Generated from D:/Python/compiler/lexanalyz\ParserGo.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ParserGo import ParserGo
else:
    from lexanalyz.gen import ParserGo

# This class defines a complete generic visitor for a parse tree produced by ParserGo.

class ParserGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ParserGo#sourceFile.
    def visitSourceFile(self, ctx:ParserGo.SourceFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#packageClause.
    def visitPackageClause(self, ctx:ParserGo.PackageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#importDecl.
    def visitImportDecl(self, ctx:ParserGo.ImportDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#importSpec.
    def visitImportSpec(self, ctx:ParserGo.ImportSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#importPath.
    def visitImportPath(self, ctx:ParserGo.ImportPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#declaration.
    def visitDeclaration(self, ctx:ParserGo.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#constDecl.
    def visitConstDecl(self, ctx:ParserGo.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#constSpec.
    def visitConstSpec(self, ctx:ParserGo.ConstSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#identifierList.
    def visitIdentifierList(self, ctx:ParserGo.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#expressionList.
    def visitExpressionList(self, ctx:ParserGo.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#typeDecl.
    def visitTypeDecl(self, ctx:ParserGo.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#typeSpec.
    def visitTypeSpec(self, ctx:ParserGo.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#functionDecl.
    def visitFunctionDecl(self, ctx:ParserGo.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#methodDecl.
    def visitMethodDecl(self, ctx:ParserGo.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#receiver.
    def visitReceiver(self, ctx:ParserGo.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#varDecl.
    def visitVarDecl(self, ctx:ParserGo.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#varSpec.
    def visitVarSpec(self, ctx:ParserGo.VarSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#block.
    def visitBlock(self, ctx:ParserGo.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#statementList.
    def visitStatementList(self, ctx:ParserGo.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#statement.
    def visitStatement(self, ctx:ParserGo.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#simpleStmt.
    def visitSimpleStmt(self, ctx:ParserGo.SimpleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#expressionStmt.
    def visitExpressionStmt(self, ctx:ParserGo.ExpressionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#sendStmt.
    def visitSendStmt(self, ctx:ParserGo.SendStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#incDecStmt.
    def visitIncDecStmt(self, ctx:ParserGo.IncDecStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#assignment.
    def visitAssignment(self, ctx:ParserGo.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#assign_op.
    def visitAssign_op(self, ctx:ParserGo.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#shortVarDecl.
    def visitShortVarDecl(self, ctx:ParserGo.ShortVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#emptyStmt.
    def visitEmptyStmt(self, ctx:ParserGo.EmptyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#labeledStmt.
    def visitLabeledStmt(self, ctx:ParserGo.LabeledStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#returnStmt.
    def visitReturnStmt(self, ctx:ParserGo.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#breakStmt.
    def visitBreakStmt(self, ctx:ParserGo.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#continueStmt.
    def visitContinueStmt(self, ctx:ParserGo.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#gotoStmt.
    def visitGotoStmt(self, ctx:ParserGo.GotoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#fallthroughStmt.
    def visitFallthroughStmt(self, ctx:ParserGo.FallthroughStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#deferStmt.
    def visitDeferStmt(self, ctx:ParserGo.DeferStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#ifStmt.
    def visitIfStmt(self, ctx:ParserGo.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#switchStmt.
    def visitSwitchStmt(self, ctx:ParserGo.SwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#exprSwitchStmt.
    def visitExprSwitchStmt(self, ctx:ParserGo.ExprSwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#exprCaseClause.
    def visitExprCaseClause(self, ctx:ParserGo.ExprCaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#exprSwitchCase.
    def visitExprSwitchCase(self, ctx:ParserGo.ExprSwitchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#typeSwitchStmt.
    def visitTypeSwitchStmt(self, ctx:ParserGo.TypeSwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#typeSwitchGuard.
    def visitTypeSwitchGuard(self, ctx:ParserGo.TypeSwitchGuardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#typeCaseClause.
    def visitTypeCaseClause(self, ctx:ParserGo.TypeCaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#typeSwitchCase.
    def visitTypeSwitchCase(self, ctx:ParserGo.TypeSwitchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#typeList.
    def visitTypeList(self, ctx:ParserGo.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#selectStmt.
    def visitSelectStmt(self, ctx:ParserGo.SelectStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#commClause.
    def visitCommClause(self, ctx:ParserGo.CommClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#commCase.
    def visitCommCase(self, ctx:ParserGo.CommCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#recvStmt.
    def visitRecvStmt(self, ctx:ParserGo.RecvStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#forStmt.
    def visitForStmt(self, ctx:ParserGo.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#forClause.
    def visitForClause(self, ctx:ParserGo.ForClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#rangeClause.
    def visitRangeClause(self, ctx:ParserGo.RangeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#goStmt.
    def visitGoStmt(self, ctx:ParserGo.GoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#type_.
    def visitType_(self, ctx:ParserGo.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#typeName.
    def visitTypeName(self, ctx:ParserGo.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#typeLit.
    def visitTypeLit(self, ctx:ParserGo.TypeLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#arrayType.
    def visitArrayType(self, ctx:ParserGo.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#arrayLength.
    def visitArrayLength(self, ctx:ParserGo.ArrayLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#elementType.
    def visitElementType(self, ctx:ParserGo.ElementTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#pointerType.
    def visitPointerType(self, ctx:ParserGo.PointerTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#interfaceType.
    def visitInterfaceType(self, ctx:ParserGo.InterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#r_sliceType.
    def visitR_sliceType(self, ctx:ParserGo.R_sliceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#mapType.
    def visitMapType(self, ctx:ParserGo.MapTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#channelType.
    def visitChannelType(self, ctx:ParserGo.ChannelTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#methodSpec.
    def visitMethodSpec(self, ctx:ParserGo.MethodSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#functionType.
    def visitFunctionType(self, ctx:ParserGo.FunctionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#signature.
    def visitSignature(self, ctx:ParserGo.SignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#result.
    def visitResult(self, ctx:ParserGo.ResultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#parameters.
    def visitParameters(self, ctx:ParserGo.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#parameterDecl.
    def visitParameterDecl(self, ctx:ParserGo.ParameterDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#expression.
    def visitExpression(self, ctx:ParserGo.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#primaryExpr.
    def visitPrimaryExpr(self, ctx:ParserGo.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#unaryExpr.
    def visitUnaryExpr(self, ctx:ParserGo.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#conversion.
    def visitConversion(self, ctx:ParserGo.ConversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#operand.
    def visitOperand(self, ctx:ParserGo.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#literal.
    def visitLiteral(self, ctx:ParserGo.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#basicLit.
    def visitBasicLit(self, ctx:ParserGo.BasicLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#integer.
    def visitInteger(self, ctx:ParserGo.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#operandName.
    def visitOperandName(self, ctx:ParserGo.OperandNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#qualifiedIdent.
    def visitQualifiedIdent(self, ctx:ParserGo.QualifiedIdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#compositeLit.
    def visitCompositeLit(self, ctx:ParserGo.CompositeLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#literalType.
    def visitLiteralType(self, ctx:ParserGo.LiteralTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#literalValue.
    def visitLiteralValue(self, ctx:ParserGo.LiteralValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#elementList.
    def visitElementList(self, ctx:ParserGo.ElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#keyedElement.
    def visitKeyedElement(self, ctx:ParserGo.KeyedElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#key.
    def visitKey(self, ctx:ParserGo.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#element.
    def visitElement(self, ctx:ParserGo.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#structType.
    def visitStructType(self, ctx:ParserGo.StructTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#fieldDecl.
    def visitFieldDecl(self, ctx:ParserGo.FieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#string_.
    def visitString_(self, ctx:ParserGo.String_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#anonymousField.
    def visitAnonymousField(self, ctx:ParserGo.AnonymousFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#functionLit.
    def visitFunctionLit(self, ctx:ParserGo.FunctionLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#index.
    def visitIndex(self, ctx:ParserGo.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#r_slice.
    def visitR_slice(self, ctx:ParserGo.R_sliceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#typeAssertion.
    def visitTypeAssertion(self, ctx:ParserGo.TypeAssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#arguments.
    def visitArguments(self, ctx:ParserGo.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#methodExpr.
    def visitMethodExpr(self, ctx:ParserGo.MethodExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#receiverType.
    def visitReceiverType(self, ctx:ParserGo.ReceiverTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGo#eos.
    def visitEos(self, ctx:ParserGo.EosContext):
        return self.visitChildren(ctx)



del ParserGo