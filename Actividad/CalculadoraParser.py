# Generated from Calculadora.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,38,8,2,1,2,1,2,1,2,
        1,2,1,2,3,2,45,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,53,8,2,10,2,12,2,
        56,9,2,1,3,1,3,1,3,1,3,3,3,62,8,3,1,3,1,3,1,3,4,3,67,8,3,11,3,12,
        3,68,1,3,1,3,1,4,1,4,1,4,5,4,76,8,4,10,4,12,4,79,9,4,1,5,1,5,1,5,
        5,5,84,8,5,10,5,12,5,87,9,5,1,5,0,1,4,6,0,2,4,6,8,10,0,2,1,0,2,3,
        1,0,4,5,96,0,13,1,0,0,0,2,29,1,0,0,0,4,44,1,0,0,0,6,57,1,0,0,0,8,
        72,1,0,0,0,10,80,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,15,1,0,0,
        0,15,13,1,0,0,0,15,16,1,0,0,0,16,1,1,0,0,0,17,18,3,4,2,0,18,19,5,
        14,0,0,19,30,1,0,0,0,20,21,5,12,0,0,21,22,5,1,0,0,22,23,3,4,2,0,
        23,24,5,14,0,0,24,30,1,0,0,0,25,26,3,6,3,0,26,27,5,14,0,0,27,30,
        1,0,0,0,28,30,5,14,0,0,29,17,1,0,0,0,29,20,1,0,0,0,29,25,1,0,0,0,
        29,28,1,0,0,0,30,3,1,0,0,0,31,32,6,2,-1,0,32,45,5,13,0,0,33,45,5,
        12,0,0,34,35,5,12,0,0,35,37,5,6,0,0,36,38,3,8,4,0,37,36,1,0,0,0,
        37,38,1,0,0,0,38,39,1,0,0,0,39,45,5,7,0,0,40,41,5,6,0,0,41,42,3,
        4,2,0,42,43,5,7,0,0,43,45,1,0,0,0,44,31,1,0,0,0,44,33,1,0,0,0,44,
        34,1,0,0,0,44,40,1,0,0,0,45,54,1,0,0,0,46,47,10,6,0,0,47,48,7,0,
        0,0,48,53,3,4,2,7,49,50,10,5,0,0,50,51,7,1,0,0,51,53,3,4,2,6,52,
        46,1,0,0,0,52,49,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,
        0,55,5,1,0,0,0,56,54,1,0,0,0,57,58,5,8,0,0,58,59,5,12,0,0,59,61,
        5,6,0,0,60,62,3,10,5,0,61,60,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,
        63,64,5,7,0,0,64,66,5,9,0,0,65,67,3,2,1,0,66,65,1,0,0,0,67,68,1,
        0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,71,5,10,0,0,71,
        7,1,0,0,0,72,77,3,4,2,0,73,74,5,11,0,0,74,76,3,4,2,0,75,73,1,0,0,
        0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,9,1,0,0,0,79,77,1,
        0,0,0,80,85,5,12,0,0,81,82,5,11,0,0,82,84,5,12,0,0,83,81,1,0,0,0,
        84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,11,1,0,0,0,87,85,1,
        0,0,0,10,15,29,37,44,52,54,61,68,77,85
    ]

class CalculadoraParser ( Parser ):

    grammarFileName = "Calculadora.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'*'", "'/'", "'+'", "'-'", "'('", 
                     "')'", "'func'", "'{'", "'}'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_funcionDef = 3
    RULE_args = 4
    RULE_params = 5

    ruleNames =  [ "prog", "stat", "expr", "funcionDef", "args", "params" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    ID=12
    INT=13
    NEWLINE=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.StatContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.StatContext,i)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = CalculadoraParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.stat()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 28992) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculadoraParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(CalculadoraParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)


    class FunctionDefinitionContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcionDef(self):
            return self.getTypedRuleContext(CalculadoraParser.FuncionDefContext,0)

        def NEWLINE(self):
            return self.getToken(CalculadoraParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(CalculadoraParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalculadoraParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(CalculadoraParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def stat(self):

        localctx = CalculadoraParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = CalculadoraParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.expr(0)
                self.state = 18
                self.match(CalculadoraParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = CalculadoraParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(CalculadoraParser.ID)
                self.state = 21
                self.match(CalculadoraParser.T__0)
                self.state = 22
                self.expr(0)
                self.state = 23
                self.match(CalculadoraParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = CalculadoraParser.FunctionDefinitionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.funcionDef()
                self.state = 26
                self.match(CalculadoraParser.NEWLINE)
                pass

            elif la_ == 4:
                localctx = CalculadoraParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.match(CalculadoraParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculadoraParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class FunctionCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalculadoraParser.ID, 0)
        def args(self):
            return self.getTypedRuleContext(CalculadoraParser.ArgsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalculadoraParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CalculadoraParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculadoraParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = CalculadoraParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 32
                self.match(CalculadoraParser.INT)
                pass

            elif la_ == 2:
                localctx = CalculadoraParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 33
                self.match(CalculadoraParser.ID)
                pass

            elif la_ == 3:
                localctx = CalculadoraParser.FunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.match(CalculadoraParser.ID)
                self.state = 35
                self.match(CalculadoraParser.T__5)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 12352) != 0):
                    self.state = 36
                    self.args()


                self.state = 39
                self.match(CalculadoraParser.T__6)
                pass

            elif la_ == 4:
                localctx = CalculadoraParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.match(CalculadoraParser.T__5)
                self.state = 41
                self.expr(0)
                self.state = 42
                self.match(CalculadoraParser.T__6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 52
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = CalculadoraParser.MulDivContext(self, CalculadoraParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 47
                        _la = self._input.LA(1)
                        if not(_la==2 or _la==3):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 48
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = CalculadoraParser.AddSubContext(self, CalculadoraParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 50
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 51
                        self.expr(6)
                        pass

             
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncionDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalculadoraParser.ID, 0)

        def params(self):
            return self.getTypedRuleContext(CalculadoraParser.ParamsContext,0)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.StatContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.StatContext,i)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_funcionDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionDef" ):
                listener.enterFuncionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionDef" ):
                listener.exitFuncionDef(self)




    def funcionDef(self):

        localctx = CalculadoraParser.FuncionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcionDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(CalculadoraParser.T__7)
            self.state = 58
            self.match(CalculadoraParser.ID)
            self.state = 59
            self.match(CalculadoraParser.T__5)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 60
                self.params()


            self.state = 63
            self.match(CalculadoraParser.T__6)
            self.state = 64
            self.match(CalculadoraParser.T__8)
            self.state = 66 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 65
                self.stat()
                self.state = 68 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 28992) != 0)):
                    break

            self.state = 70
            self.match(CalculadoraParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExprContext,i)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = CalculadoraParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.expr(0)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 73
                self.match(CalculadoraParser.T__10)
                self.state = 74
                self.expr(0)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CalculadoraParser.ID)
            else:
                return self.getToken(CalculadoraParser.ID, i)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = CalculadoraParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(CalculadoraParser.ID)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 81
                self.match(CalculadoraParser.T__10)
                self.state = 82
                self.match(CalculadoraParser.ID)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




