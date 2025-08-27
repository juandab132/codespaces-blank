# Generated from Calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete listener for a parse tree produced by CalculadoraParser.
class CalculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by CalculadoraParser#prog.
    def enterProg(self, ctx:CalculadoraParser.ProgContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#prog.
    def exitProg(self, ctx:CalculadoraParser.ProgContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#printExpr.
    def enterPrintExpr(self, ctx:CalculadoraParser.PrintExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#printExpr.
    def exitPrintExpr(self, ctx:CalculadoraParser.PrintExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#assign.
    def enterAssign(self, ctx:CalculadoraParser.AssignContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#assign.
    def exitAssign(self, ctx:CalculadoraParser.AssignContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CalculadoraParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CalculadoraParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#blank.
    def enterBlank(self, ctx:CalculadoraParser.BlankContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#blank.
    def exitBlank(self, ctx:CalculadoraParser.BlankContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#parens.
    def enterParens(self, ctx:CalculadoraParser.ParensContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#parens.
    def exitParens(self, ctx:CalculadoraParser.ParensContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#MulDiv.
    def enterMulDiv(self, ctx:CalculadoraParser.MulDivContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#MulDiv.
    def exitMulDiv(self, ctx:CalculadoraParser.MulDivContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#AddSub.
    def enterAddSub(self, ctx:CalculadoraParser.AddSubContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#AddSub.
    def exitAddSub(self, ctx:CalculadoraParser.AddSubContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#functionCall.
    def enterFunctionCall(self, ctx:CalculadoraParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#functionCall.
    def exitFunctionCall(self, ctx:CalculadoraParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#id.
    def enterId(self, ctx:CalculadoraParser.IdContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#id.
    def exitId(self, ctx:CalculadoraParser.IdContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#int.
    def enterInt(self, ctx:CalculadoraParser.IntContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#int.
    def exitInt(self, ctx:CalculadoraParser.IntContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#funcionDef.
    def enterFuncionDef(self, ctx:CalculadoraParser.FuncionDefContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#funcionDef.
    def exitFuncionDef(self, ctx:CalculadoraParser.FuncionDefContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#args.
    def enterArgs(self, ctx:CalculadoraParser.ArgsContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#args.
    def exitArgs(self, ctx:CalculadoraParser.ArgsContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#params.
    def enterParams(self, ctx:CalculadoraParser.ParamsContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#params.
    def exitParams(self, ctx:CalculadoraParser.ParamsContext):
        pass



del CalculadoraParser