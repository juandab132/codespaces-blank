# Generated from Impuestos.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ImpuestosParser import ImpuestosParser
else:
    from ImpuestosParser import ImpuestosParser

# This class defines a complete listener for a parse tree produced by ImpuestosParser.
class ImpuestosListener(ParseTreeListener):

    # Enter a parse tree produced by ImpuestosParser#program.
    def enterProgram(self, ctx:ImpuestosParser.ProgramContext):
        pass

    # Exit a parse tree produced by ImpuestosParser#program.
    def exitProgram(self, ctx:ImpuestosParser.ProgramContext):
        pass


    # Enter a parse tree produced by ImpuestosParser#statement.
    def enterStatement(self, ctx:ImpuestosParser.StatementContext):
        pass

    # Exit a parse tree produced by ImpuestosParser#statement.
    def exitStatement(self, ctx:ImpuestosParser.StatementContext):
        pass


    # Enter a parse tree produced by ImpuestosParser#assignment.
    def enterAssignment(self, ctx:ImpuestosParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ImpuestosParser#assignment.
    def exitAssignment(self, ctx:ImpuestosParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ImpuestosParser#ifStatement.
    def enterIfStatement(self, ctx:ImpuestosParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ImpuestosParser#ifStatement.
    def exitIfStatement(self, ctx:ImpuestosParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ImpuestosParser#printStatement.
    def enterPrintStatement(self, ctx:ImpuestosParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by ImpuestosParser#printStatement.
    def exitPrintStatement(self, ctx:ImpuestosParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by ImpuestosParser#condition.
    def enterCondition(self, ctx:ImpuestosParser.ConditionContext):
        pass

    # Exit a parse tree produced by ImpuestosParser#condition.
    def exitCondition(self, ctx:ImpuestosParser.ConditionContext):
        pass


    # Enter a parse tree produced by ImpuestosParser#expr.
    def enterExpr(self, ctx:ImpuestosParser.ExprContext):
        pass

    # Exit a parse tree produced by ImpuestosParser#expr.
    def exitExpr(self, ctx:ImpuestosParser.ExprContext):
        pass


    # Enter a parse tree produced by ImpuestosParser#term.
    def enterTerm(self, ctx:ImpuestosParser.TermContext):
        pass

    # Exit a parse tree produced by ImpuestosParser#term.
    def exitTerm(self, ctx:ImpuestosParser.TermContext):
        pass


    # Enter a parse tree produced by ImpuestosParser#op.
    def enterOp(self, ctx:ImpuestosParser.OpContext):
        pass

    # Exit a parse tree produced by ImpuestosParser#op.
    def exitOp(self, ctx:ImpuestosParser.OpContext):
        pass


    # Enter a parse tree produced by ImpuestosParser#comparator.
    def enterComparator(self, ctx:ImpuestosParser.ComparatorContext):
        pass

    # Exit a parse tree produced by ImpuestosParser#comparator.
    def exitComparator(self, ctx:ImpuestosParser.ComparatorContext):
        pass



del ImpuestosParser