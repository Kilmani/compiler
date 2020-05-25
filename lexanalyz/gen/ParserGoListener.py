# Generated from D:/Python/compiler/lexanalyz\ParserGo.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ParserGo import ParserGo
else:
    from lexanalyz.gen.ParserGo import *

# This class defines a complete listener for a parse tree produced by ParserGo.
class ParserGoListener(ParseTreeListener):

    # Enter a parse tree produced by ParserGo#sourceFile.
    def enterSourceFile(self, ctx:ParserGo.SourceFileContext):
        pass

    # Exit a parse tree produced by ParserGo#sourceFile.
    def exitSourceFile(self, ctx:ParserGo.SourceFileContext):
        pass


    # Enter a parse tree produced by ParserGo#packageClause.
    def enterPackageClause(self, ctx:ParserGo.PackageClauseContext):
        pass

    # Exit a parse tree produced by ParserGo#packageClause.
    def exitPackageClause(self, ctx:ParserGo.PackageClauseContext):
        pass


    # Enter a parse tree produced by ParserGo#importDecl.
    def enterImportDecl(self, ctx:ParserGo.ImportDeclContext):
        pass

    # Exit a parse tree produced by ParserGo#importDecl.
    def exitImportDecl(self, ctx:ParserGo.ImportDeclContext):
        pass


    # Enter a parse tree produced by ParserGo#importSpec.
    def enterImportSpec(self, ctx:ParserGo.ImportSpecContext):
        pass

    # Exit a parse tree produced by ParserGo#importSpec.
    def exitImportSpec(self, ctx:ParserGo.ImportSpecContext):
        pass


    # Enter a parse tree produced by ParserGo#importPath.
    def enterImportPath(self, ctx:ParserGo.ImportPathContext):
        pass

    # Exit a parse tree produced by ParserGo#importPath.
    def exitImportPath(self, ctx:ParserGo.ImportPathContext):
        pass


    # Enter a parse tree produced by ParserGo#declaration.
    def enterDeclaration(self, ctx:ParserGo.DeclarationContext):
        pass

    # Exit a parse tree produced by ParserGo#declaration.
    def exitDeclaration(self, ctx:ParserGo.DeclarationContext):
        pass


    # Enter a parse tree produced by ParserGo#constDecl.
    def enterConstDecl(self, ctx:ParserGo.ConstDeclContext):
        pass

    # Exit a parse tree produced by ParserGo#constDecl.
    def exitConstDecl(self, ctx:ParserGo.ConstDeclContext):
        pass


    # Enter a parse tree produced by ParserGo#constSpec.
    def enterConstSpec(self, ctx:ParserGo.ConstSpecContext):
        pass

    # Exit a parse tree produced by ParserGo#constSpec.
    def exitConstSpec(self, ctx:ParserGo.ConstSpecContext):
        pass


    # Enter a parse tree produced by ParserGo#identifierList.
    def enterIdentifierList(self, ctx:ParserGo.IdentifierListContext):
        pass

    # Exit a parse tree produced by ParserGo#identifierList.
    def exitIdentifierList(self, ctx:ParserGo.IdentifierListContext):
        pass


    # Enter a parse tree produced by ParserGo#expressionList.
    def enterExpressionList(self, ctx:ParserGo.ExpressionListContext):
        pass

    # Exit a parse tree produced by ParserGo#expressionList.
    def exitExpressionList(self, ctx:ParserGo.ExpressionListContext):
        pass


    # Enter a parse tree produced by ParserGo#typeDecl.
    def enterTypeDecl(self, ctx:ParserGo.TypeDeclContext):
        pass

    # Exit a parse tree produced by ParserGo#typeDecl.
    def exitTypeDecl(self, ctx:ParserGo.TypeDeclContext):
        pass


    # Enter a parse tree produced by ParserGo#typeSpec.
    def enterTypeSpec(self, ctx:ParserGo.TypeSpecContext):
        pass

    # Exit a parse tree produced by ParserGo#typeSpec.
    def exitTypeSpec(self, ctx:ParserGo.TypeSpecContext):
        pass


    # Enter a parse tree produced by ParserGo#functionDecl.
    def enterFunctionDecl(self, ctx:ParserGo.FunctionDeclContext):
        pass

    # Exit a parse tree produced by ParserGo#functionDecl.
    def exitFunctionDecl(self, ctx:ParserGo.FunctionDeclContext):
        pass


    # Enter a parse tree produced by ParserGo#methodDecl.
    def enterMethodDecl(self, ctx:ParserGo.MethodDeclContext):
        pass

    # Exit a parse tree produced by ParserGo#methodDecl.
    def exitMethodDecl(self, ctx:ParserGo.MethodDeclContext):
        pass


    # Enter a parse tree produced by ParserGo#receiver.
    def enterReceiver(self, ctx:ParserGo.ReceiverContext):
        pass

    # Exit a parse tree produced by ParserGo#receiver.
    def exitReceiver(self, ctx:ParserGo.ReceiverContext):
        pass


    # Enter a parse tree produced by ParserGo#varDecl.
    def enterVarDecl(self, ctx:ParserGo.VarDeclContext):
        pass

    # Exit a parse tree produced by ParserGo#varDecl.
    def exitVarDecl(self, ctx:ParserGo.VarDeclContext):
        pass


    # Enter a parse tree produced by ParserGo#varSpec.
    def enterVarSpec(self, ctx:ParserGo.VarSpecContext):
        pass

    # Exit a parse tree produced by ParserGo#varSpec.
    def exitVarSpec(self, ctx:ParserGo.VarSpecContext):
        pass


    # Enter a parse tree produced by ParserGo#block.
    def enterBlock(self, ctx:ParserGo.BlockContext):
        pass

    # Exit a parse tree produced by ParserGo#block.
    def exitBlock(self, ctx:ParserGo.BlockContext):
        pass


    # Enter a parse tree produced by ParserGo#statementList.
    def enterStatementList(self, ctx:ParserGo.StatementListContext):
        pass

    # Exit a parse tree produced by ParserGo#statementList.
    def exitStatementList(self, ctx:ParserGo.StatementListContext):
        pass


    # Enter a parse tree produced by ParserGo#statement.
    def enterStatement(self, ctx:ParserGo.StatementContext):
        pass

    # Exit a parse tree produced by ParserGo#statement.
    def exitStatement(self, ctx:ParserGo.StatementContext):
        pass


    # Enter a parse tree produced by ParserGo#simpleStmt.
    def enterSimpleStmt(self, ctx:ParserGo.SimpleStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#simpleStmt.
    def exitSimpleStmt(self, ctx:ParserGo.SimpleStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#expressionStmt.
    def enterExpressionStmt(self, ctx:ParserGo.ExpressionStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#expressionStmt.
    def exitExpressionStmt(self, ctx:ParserGo.ExpressionStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#sendStmt.
    def enterSendStmt(self, ctx:ParserGo.SendStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#sendStmt.
    def exitSendStmt(self, ctx:ParserGo.SendStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#incDecStmt.
    def enterIncDecStmt(self, ctx:ParserGo.IncDecStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#incDecStmt.
    def exitIncDecStmt(self, ctx:ParserGo.IncDecStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#assignment.
    def enterAssignment(self, ctx:ParserGo.AssignmentContext):
        pass

    # Exit a parse tree produced by ParserGo#assignment.
    def exitAssignment(self, ctx:ParserGo.AssignmentContext):
        pass


    # Enter a parse tree produced by ParserGo#assign_op.
    def enterAssign_op(self, ctx:ParserGo.Assign_opContext):
        pass

    # Exit a parse tree produced by ParserGo#assign_op.
    def exitAssign_op(self, ctx:ParserGo.Assign_opContext):
        pass


    # Enter a parse tree produced by ParserGo#shortVarDecl.
    def enterShortVarDecl(self, ctx:ParserGo.ShortVarDeclContext):
        pass

    # Exit a parse tree produced by ParserGo#shortVarDecl.
    def exitShortVarDecl(self, ctx:ParserGo.ShortVarDeclContext):
        pass


    # Enter a parse tree produced by ParserGo#emptyStmt.
    def enterEmptyStmt(self, ctx:ParserGo.EmptyStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#emptyStmt.
    def exitEmptyStmt(self, ctx:ParserGo.EmptyStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#labeledStmt.
    def enterLabeledStmt(self, ctx:ParserGo.LabeledStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#labeledStmt.
    def exitLabeledStmt(self, ctx:ParserGo.LabeledStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#returnStmt.
    def enterReturnStmt(self, ctx:ParserGo.ReturnStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#returnStmt.
    def exitReturnStmt(self, ctx:ParserGo.ReturnStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#breakStmt.
    def enterBreakStmt(self, ctx:ParserGo.BreakStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#breakStmt.
    def exitBreakStmt(self, ctx:ParserGo.BreakStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#continueStmt.
    def enterContinueStmt(self, ctx:ParserGo.ContinueStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#continueStmt.
    def exitContinueStmt(self, ctx:ParserGo.ContinueStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#gotoStmt.
    def enterGotoStmt(self, ctx:ParserGo.GotoStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#gotoStmt.
    def exitGotoStmt(self, ctx:ParserGo.GotoStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#fallthroughStmt.
    def enterFallthroughStmt(self, ctx:ParserGo.FallthroughStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#fallthroughStmt.
    def exitFallthroughStmt(self, ctx:ParserGo.FallthroughStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#deferStmt.
    def enterDeferStmt(self, ctx:ParserGo.DeferStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#deferStmt.
    def exitDeferStmt(self, ctx:ParserGo.DeferStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#ifStmt.
    def enterIfStmt(self, ctx:ParserGo.IfStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#ifStmt.
    def exitIfStmt(self, ctx:ParserGo.IfStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#switchStmt.
    def enterSwitchStmt(self, ctx:ParserGo.SwitchStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#switchStmt.
    def exitSwitchStmt(self, ctx:ParserGo.SwitchStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#exprSwitchStmt.
    def enterExprSwitchStmt(self, ctx:ParserGo.ExprSwitchStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#exprSwitchStmt.
    def exitExprSwitchStmt(self, ctx:ParserGo.ExprSwitchStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#exprCaseClause.
    def enterExprCaseClause(self, ctx:ParserGo.ExprCaseClauseContext):
        pass

    # Exit a parse tree produced by ParserGo#exprCaseClause.
    def exitExprCaseClause(self, ctx:ParserGo.ExprCaseClauseContext):
        pass


    # Enter a parse tree produced by ParserGo#exprSwitchCase.
    def enterExprSwitchCase(self, ctx:ParserGo.ExprSwitchCaseContext):
        pass

    # Exit a parse tree produced by ParserGo#exprSwitchCase.
    def exitExprSwitchCase(self, ctx:ParserGo.ExprSwitchCaseContext):
        pass


    # Enter a parse tree produced by ParserGo#typeSwitchStmt.
    def enterTypeSwitchStmt(self, ctx:ParserGo.TypeSwitchStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#typeSwitchStmt.
    def exitTypeSwitchStmt(self, ctx:ParserGo.TypeSwitchStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#typeSwitchGuard.
    def enterTypeSwitchGuard(self, ctx:ParserGo.TypeSwitchGuardContext):
        pass

    # Exit a parse tree produced by ParserGo#typeSwitchGuard.
    def exitTypeSwitchGuard(self, ctx:ParserGo.TypeSwitchGuardContext):
        pass


    # Enter a parse tree produced by ParserGo#typeCaseClause.
    def enterTypeCaseClause(self, ctx:ParserGo.TypeCaseClauseContext):
        pass

    # Exit a parse tree produced by ParserGo#typeCaseClause.
    def exitTypeCaseClause(self, ctx:ParserGo.TypeCaseClauseContext):
        pass


    # Enter a parse tree produced by ParserGo#typeSwitchCase.
    def enterTypeSwitchCase(self, ctx:ParserGo.TypeSwitchCaseContext):
        pass

    # Exit a parse tree produced by ParserGo#typeSwitchCase.
    def exitTypeSwitchCase(self, ctx:ParserGo.TypeSwitchCaseContext):
        pass


    # Enter a parse tree produced by ParserGo#typeList.
    def enterTypeList(self, ctx:ParserGo.TypeListContext):
        pass

    # Exit a parse tree produced by ParserGo#typeList.
    def exitTypeList(self, ctx:ParserGo.TypeListContext):
        pass


    # Enter a parse tree produced by ParserGo#selectStmt.
    def enterSelectStmt(self, ctx:ParserGo.SelectStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#selectStmt.
    def exitSelectStmt(self, ctx:ParserGo.SelectStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#commClause.
    def enterCommClause(self, ctx:ParserGo.CommClauseContext):
        pass

    # Exit a parse tree produced by ParserGo#commClause.
    def exitCommClause(self, ctx:ParserGo.CommClauseContext):
        pass


    # Enter a parse tree produced by ParserGo#commCase.
    def enterCommCase(self, ctx:ParserGo.CommCaseContext):
        pass

    # Exit a parse tree produced by ParserGo#commCase.
    def exitCommCase(self, ctx:ParserGo.CommCaseContext):
        pass


    # Enter a parse tree produced by ParserGo#recvStmt.
    def enterRecvStmt(self, ctx:ParserGo.RecvStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#recvStmt.
    def exitRecvStmt(self, ctx:ParserGo.RecvStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#forStmt.
    def enterForStmt(self, ctx:ParserGo.ForStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#forStmt.
    def exitForStmt(self, ctx:ParserGo.ForStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#forClause.
    def enterForClause(self, ctx:ParserGo.ForClauseContext):
        pass

    # Exit a parse tree produced by ParserGo#forClause.
    def exitForClause(self, ctx:ParserGo.ForClauseContext):
        pass


    # Enter a parse tree produced by ParserGo#rangeClause.
    def enterRangeClause(self, ctx:ParserGo.RangeClauseContext):
        pass

    # Exit a parse tree produced by ParserGo#rangeClause.
    def exitRangeClause(self, ctx:ParserGo.RangeClauseContext):
        pass


    # Enter a parse tree produced by ParserGo#goStmt.
    def enterGoStmt(self, ctx:ParserGo.GoStmtContext):
        pass

    # Exit a parse tree produced by ParserGo#goStmt.
    def exitGoStmt(self, ctx:ParserGo.GoStmtContext):
        pass


    # Enter a parse tree produced by ParserGo#type_.
    def enterType_(self, ctx:ParserGo.Type_Context):
        pass

    # Exit a parse tree produced by ParserGo#type_.
    def exitType_(self, ctx:ParserGo.Type_Context):
        pass


    # Enter a parse tree produced by ParserGo#typeName.
    def enterTypeName(self, ctx:ParserGo.TypeNameContext):
        pass

    # Exit a parse tree produced by ParserGo#typeName.
    def exitTypeName(self, ctx:ParserGo.TypeNameContext):
        pass


    # Enter a parse tree produced by ParserGo#typeLit.
    def enterTypeLit(self, ctx:ParserGo.TypeLitContext):
        pass

    # Exit a parse tree produced by ParserGo#typeLit.
    def exitTypeLit(self, ctx:ParserGo.TypeLitContext):
        pass


    # Enter a parse tree produced by ParserGo#arrayType.
    def enterArrayType(self, ctx:ParserGo.ArrayTypeContext):
        pass

    # Exit a parse tree produced by ParserGo#arrayType.
    def exitArrayType(self, ctx:ParserGo.ArrayTypeContext):
        pass


    # Enter a parse tree produced by ParserGo#arrayLength.
    def enterArrayLength(self, ctx:ParserGo.ArrayLengthContext):
        pass

    # Exit a parse tree produced by ParserGo#arrayLength.
    def exitArrayLength(self, ctx:ParserGo.ArrayLengthContext):
        pass


    # Enter a parse tree produced by ParserGo#elementType.
    def enterElementType(self, ctx:ParserGo.ElementTypeContext):
        pass

    # Exit a parse tree produced by ParserGo#elementType.
    def exitElementType(self, ctx:ParserGo.ElementTypeContext):
        pass


    # Enter a parse tree produced by ParserGo#pointerType.
    def enterPointerType(self, ctx:ParserGo.PointerTypeContext):
        pass

    # Exit a parse tree produced by ParserGo#pointerType.
    def exitPointerType(self, ctx:ParserGo.PointerTypeContext):
        pass


    # Enter a parse tree produced by ParserGo#interfaceType.
    def enterInterfaceType(self, ctx:ParserGo.InterfaceTypeContext):
        pass

    # Exit a parse tree produced by ParserGo#interfaceType.
    def exitInterfaceType(self, ctx:ParserGo.InterfaceTypeContext):
        pass


    # Enter a parse tree produced by ParserGo#r_sliceType.
    def enterR_sliceType(self, ctx:ParserGo.R_sliceTypeContext):
        pass

    # Exit a parse tree produced by ParserGo#r_sliceType.
    def exitR_sliceType(self, ctx:ParserGo.R_sliceTypeContext):
        pass


    # Enter a parse tree produced by ParserGo#mapType.
    def enterMapType(self, ctx:ParserGo.MapTypeContext):
        pass

    # Exit a parse tree produced by ParserGo#mapType.
    def exitMapType(self, ctx:ParserGo.MapTypeContext):
        pass


    # Enter a parse tree produced by ParserGo#channelType.
    def enterChannelType(self, ctx:ParserGo.ChannelTypeContext):
        pass

    # Exit a parse tree produced by ParserGo#channelType.
    def exitChannelType(self, ctx:ParserGo.ChannelTypeContext):
        pass


    # Enter a parse tree produced by ParserGo#methodSpec.
    def enterMethodSpec(self, ctx:ParserGo.MethodSpecContext):
        pass

    # Exit a parse tree produced by ParserGo#methodSpec.
    def exitMethodSpec(self, ctx:ParserGo.MethodSpecContext):
        pass


    # Enter a parse tree produced by ParserGo#functionType.
    def enterFunctionType(self, ctx:ParserGo.FunctionTypeContext):
        pass

    # Exit a parse tree produced by ParserGo#functionType.
    def exitFunctionType(self, ctx:ParserGo.FunctionTypeContext):
        pass


    # Enter a parse tree produced by ParserGo#signature.
    def enterSignature(self, ctx:ParserGo.SignatureContext):
        pass

    # Exit a parse tree produced by ParserGo#signature.
    def exitSignature(self, ctx:ParserGo.SignatureContext):
        pass


    # Enter a parse tree produced by ParserGo#result.
    def enterResult(self, ctx:ParserGo.ResultContext):
        pass

    # Exit a parse tree produced by ParserGo#result.
    def exitResult(self, ctx:ParserGo.ResultContext):
        pass


    # Enter a parse tree produced by ParserGo#parameters.
    def enterParameters(self, ctx:ParserGo.ParametersContext):
        pass

    # Exit a parse tree produced by ParserGo#parameters.
    def exitParameters(self, ctx:ParserGo.ParametersContext):
        pass


    # Enter a parse tree produced by ParserGo#parameterDecl.
    def enterParameterDecl(self, ctx:ParserGo.ParameterDeclContext):
        pass

    # Exit a parse tree produced by ParserGo#parameterDecl.
    def exitParameterDecl(self, ctx:ParserGo.ParameterDeclContext):
        pass


    # Enter a parse tree produced by ParserGo#expression.
    def enterExpression(self, ctx:ParserGo.ExpressionContext):
        pass

    # Exit a parse tree produced by ParserGo#expression.
    def exitExpression(self, ctx:ParserGo.ExpressionContext):
        pass


    # Enter a parse tree produced by ParserGo#primaryExpr.
    def enterPrimaryExpr(self, ctx:ParserGo.PrimaryExprContext):
        pass

    # Exit a parse tree produced by ParserGo#primaryExpr.
    def exitPrimaryExpr(self, ctx:ParserGo.PrimaryExprContext):
        pass


    # Enter a parse tree produced by ParserGo#unaryExpr.
    def enterUnaryExpr(self, ctx:ParserGo.UnaryExprContext):
        pass

    # Exit a parse tree produced by ParserGo#unaryExpr.
    def exitUnaryExpr(self, ctx:ParserGo.UnaryExprContext):
        pass


    # Enter a parse tree produced by ParserGo#conversion.
    def enterConversion(self, ctx:ParserGo.ConversionContext):
        pass

    # Exit a parse tree produced by ParserGo#conversion.
    def exitConversion(self, ctx:ParserGo.ConversionContext):
        pass


    # Enter a parse tree produced by ParserGo#operand.
    def enterOperand(self, ctx:ParserGo.OperandContext):
        pass

    # Exit a parse tree produced by ParserGo#operand.
    def exitOperand(self, ctx:ParserGo.OperandContext):
        pass


    # Enter a parse tree produced by ParserGo#literal.
    def enterLiteral(self, ctx:ParserGo.LiteralContext):
        pass

    # Exit a parse tree produced by ParserGo#literal.
    def exitLiteral(self, ctx:ParserGo.LiteralContext):
        pass


    # Enter a parse tree produced by ParserGo#basicLit.
    def enterBasicLit(self, ctx:ParserGo.BasicLitContext):
        pass

    # Exit a parse tree produced by ParserGo#basicLit.
    def exitBasicLit(self, ctx:ParserGo.BasicLitContext):
        pass


    # Enter a parse tree produced by ParserGo#integer.
    def enterInteger(self, ctx:ParserGo.IntegerContext):
        pass

    # Exit a parse tree produced by ParserGo#integer.
    def exitInteger(self, ctx:ParserGo.IntegerContext):
        pass


    # Enter a parse tree produced by ParserGo#operandName.
    def enterOperandName(self, ctx:ParserGo.OperandNameContext):
        pass

    # Exit a parse tree produced by ParserGo#operandName.
    def exitOperandName(self, ctx:ParserGo.OperandNameContext):
        pass


    # Enter a parse tree produced by ParserGo#qualifiedIdent.
    def enterQualifiedIdent(self, ctx:ParserGo.QualifiedIdentContext):
        pass

    # Exit a parse tree produced by ParserGo#qualifiedIdent.
    def exitQualifiedIdent(self, ctx:ParserGo.QualifiedIdentContext):
        pass


    # Enter a parse tree produced by ParserGo#compositeLit.
    def enterCompositeLit(self, ctx:ParserGo.CompositeLitContext):
        pass

    # Exit a parse tree produced by ParserGo#compositeLit.
    def exitCompositeLit(self, ctx:ParserGo.CompositeLitContext):
        pass


    # Enter a parse tree produced by ParserGo#literalType.
    def enterLiteralType(self, ctx:ParserGo.LiteralTypeContext):
        pass

    # Exit a parse tree produced by ParserGo#literalType.
    def exitLiteralType(self, ctx:ParserGo.LiteralTypeContext):
        pass


    # Enter a parse tree produced by ParserGo#literalValue.
    def enterLiteralValue(self, ctx:ParserGo.LiteralValueContext):
        pass

    # Exit a parse tree produced by ParserGo#literalValue.
    def exitLiteralValue(self, ctx:ParserGo.LiteralValueContext):
        pass


    # Enter a parse tree produced by ParserGo#elementList.
    def enterElementList(self, ctx:ParserGo.ElementListContext):
        pass

    # Exit a parse tree produced by ParserGo#elementList.
    def exitElementList(self, ctx:ParserGo.ElementListContext):
        pass


    # Enter a parse tree produced by ParserGo#keyedElement.
    def enterKeyedElement(self, ctx:ParserGo.KeyedElementContext):
        pass

    # Exit a parse tree produced by ParserGo#keyedElement.
    def exitKeyedElement(self, ctx:ParserGo.KeyedElementContext):
        pass


    # Enter a parse tree produced by ParserGo#key.
    def enterKey(self, ctx:ParserGo.KeyContext):
        pass

    # Exit a parse tree produced by ParserGo#key.
    def exitKey(self, ctx:ParserGo.KeyContext):
        pass


    # Enter a parse tree produced by ParserGo#element.
    def enterElement(self, ctx:ParserGo.ElementContext):
        pass

    # Exit a parse tree produced by ParserGo#element.
    def exitElement(self, ctx:ParserGo.ElementContext):
        pass


    # Enter a parse tree produced by ParserGo#structType.
    def enterStructType(self, ctx:ParserGo.StructTypeContext):
        pass

    # Exit a parse tree produced by ParserGo#structType.
    def exitStructType(self, ctx:ParserGo.StructTypeContext):
        pass


    # Enter a parse tree produced by ParserGo#fieldDecl.
    def enterFieldDecl(self, ctx:ParserGo.FieldDeclContext):
        pass

    # Exit a parse tree produced by ParserGo#fieldDecl.
    def exitFieldDecl(self, ctx:ParserGo.FieldDeclContext):
        pass


    # Enter a parse tree produced by ParserGo#string_.
    def enterString_(self, ctx:ParserGo.String_Context):
        pass

    # Exit a parse tree produced by ParserGo#string_.
    def exitString_(self, ctx:ParserGo.String_Context):
        pass


    # Enter a parse tree produced by ParserGo#anonymousField.
    def enterAnonymousField(self, ctx:ParserGo.AnonymousFieldContext):
        pass

    # Exit a parse tree produced by ParserGo#anonymousField.
    def exitAnonymousField(self, ctx:ParserGo.AnonymousFieldContext):
        pass


    # Enter a parse tree produced by ParserGo#functionLit.
    def enterFunctionLit(self, ctx:ParserGo.FunctionLitContext):
        pass

    # Exit a parse tree produced by ParserGo#functionLit.
    def exitFunctionLit(self, ctx:ParserGo.FunctionLitContext):
        pass


    # Enter a parse tree produced by ParserGo#index.
    def enterIndex(self, ctx:ParserGo.IndexContext):
        pass

    # Exit a parse tree produced by ParserGo#index.
    def exitIndex(self, ctx:ParserGo.IndexContext):
        pass


    # Enter a parse tree produced by ParserGo#r_slice.
    def enterR_slice(self, ctx:ParserGo.R_sliceContext):
        pass

    # Exit a parse tree produced by ParserGo#r_slice.
    def exitR_slice(self, ctx:ParserGo.R_sliceContext):
        pass


    # Enter a parse tree produced by ParserGo#typeAssertion.
    def enterTypeAssertion(self, ctx:ParserGo.TypeAssertionContext):
        pass

    # Exit a parse tree produced by ParserGo#typeAssertion.
    def exitTypeAssertion(self, ctx:ParserGo.TypeAssertionContext):
        pass


    # Enter a parse tree produced by ParserGo#arguments.
    def enterArguments(self, ctx:ParserGo.ArgumentsContext):
        pass

    # Exit a parse tree produced by ParserGo#arguments.
    def exitArguments(self, ctx:ParserGo.ArgumentsContext):
        pass


    # Enter a parse tree produced by ParserGo#methodExpr.
    def enterMethodExpr(self, ctx:ParserGo.MethodExprContext):
        pass

    # Exit a parse tree produced by ParserGo#methodExpr.
    def exitMethodExpr(self, ctx:ParserGo.MethodExprContext):
        pass


    # Enter a parse tree produced by ParserGo#receiverType.
    def enterReceiverType(self, ctx:ParserGo.ReceiverTypeContext):
        pass

    # Exit a parse tree produced by ParserGo#receiverType.
    def exitReceiverType(self, ctx:ParserGo.ReceiverTypeContext):
        pass


    # Enter a parse tree produced by ParserGo#eos.
    def enterEos(self, ctx:ParserGo.EosContext):
        pass

    # Exit a parse tree produced by ParserGo#eos.
    def exitEos(self, ctx:ParserGo.EosContext):
        pass



del ParserGo