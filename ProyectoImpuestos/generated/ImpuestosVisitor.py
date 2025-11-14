# Generated from Impuestos.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ImpuestosParser import ImpuestosParser
else:
    from ImpuestosParser import ImpuestosParser

# This class defines a complete generic visitor for a parse tree produced by ImpuestosParser.

class ImpuestosVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ImpuestosParser#program.
    def visitProgram(self, ctx:ImpuestosParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpuestosParser#statement.
    def visitStatement(self, ctx:ImpuestosParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpuestosParser#assignment.
    def visitAssignment(self, ctx:ImpuestosParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpuestosParser#ifStatement.
    def visitIfStatement(self, ctx:ImpuestosParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpuestosParser#printStatement.
    def visitPrintStatement(self, ctx:ImpuestosParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpuestosParser#condition.
    def visitCondition(self, ctx:ImpuestosParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpuestosParser#expr.
    def visitExpr(self, ctx:ImpuestosParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpuestosParser#term.
    def visitTerm(self, ctx:ImpuestosParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpuestosParser#op.
    def visitOp(self, ctx:ImpuestosParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpuestosParser#comparator.
    def visitComparator(self, ctx:ImpuestosParser.ComparatorContext):
        return self.visitChildren(ctx)



del ImpuestosParser