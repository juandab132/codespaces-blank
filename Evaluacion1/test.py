from antlr4 import InputStream, CommonTokenStream
from antlr4.Token import Token
from antlr4.tree.Tree import TerminalNode

from IfElseLangLexer import IfElseLangLexer
from IfElseLangParser import IfElseLangParser

code = """\
a = 10;
b = 20;
if (a > b) {
  max = a;
} else {
  if (a == b) {
    max = a;
  } else {
    max = b;
  }
}
"""

lexer = IfElseLangLexer(InputStream(code))
tokens = CommonTokenStream(lexer); tokens.fill()

print("## TOKENS")
for t in tokens.tokens:
    if t.type != Token.EOF:
        print(f"{lexer.symbolicNames[t.type]} '{t.text}' @ {t.line}:{t.column}")

parser = IfElseLangParser(tokens)
tree = parser.program()

print("\n## toStringTree")
print(tree.toStringTree(recog=parser))

def pretty(n, names, lvl=0):
    if isinstance(n, TerminalNode): return "  "*lvl + f"TOKEN({n.getText()})"
    out = "  "*lvl + names[n.getRuleIndex()]
    for c in n.children or []: out += "\n" + pretty(c, names, lvl+1)
    return out

print("\n## Árbol indentado")
print(pretty(tree, parser.ruleNames))
