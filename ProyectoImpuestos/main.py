from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener, ConsoleErrorListener

from generated.ImpuestosLexer import ImpuestosLexer
from generated.ImpuestosParser import ImpuestosParser
from generated.ImpuestosVisitor import ImpuestosVisitor

from semantic_analyzer.semantic_checker import SemanticAnalyzer
from codegen.intermediate_code import IntermediateCode
from codegen.python_generator import PythonGenerator

import sys, os

# ==============================
#  Error listener que acumula errores léxicos/sintácticos
# ==============================
class CollectingErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []  # aquí guardamos los mensajes de error detectados

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # ANTLR nos llama aquí por cada error léxico/sintáctico
        self.errors.append(f"line {line}:{column} {msg}")

    @property
    def has_errors(self):
        # True si hay al menos un error acumulado
        return len(self.errors) > 0


# ==============================
#  VISITOR PERSONALIZADO (recorre el AST y dispara semántica/IR/Python)
# ==============================
class ImpuestosCustomVisitor(ImpuestosVisitor):
    def __init__(self, semantic, inter, pygen):
        self.semantic = semantic     # analizador semántico (tabla de símbolos, errores)
        self.inter = inter           # generador/almacenador del IR (TAC)
        self.pygen = pygen           # generador de líneas Python
        self.indent = 0              # nivel de indentación para el Python generado

    # Helpers
    def _expr_text(self, ctx):              # expr -> string (texto plano del subárbol)
        return ctx.getText()

    def _cond_text_from_condition(self, cond_ctx):  # condition: ID comparator expr
        var = cond_ctx.ID().getText()
        comp = cond_ctx.comparator().getText()
        rhs = self._expr_text(cond_ctx.expr())
        return f"{var} {comp} {rhs}"

    # program: (statement)+ EOF
    def visitProgram(self, ctx):
        # Recorremos todas las sentencias del programa en orden
        if hasattr(ctx, "statement"):
            for st in ctx.statement():
                self.visit(st)
        else:
            for ch in ctx.getChildren():
                self.visit(ch)
        return None

    # assignment: ID '=' expr ';'
    def visitAssignment(self, ctx):
        # Validar primero los IDs usados en RHS (expr) antes de declarar
        self.visit(ctx.expr())
        var = ctx.ID().getText()
        expr_text = self._expr_text(ctx.expr())
        # Declaración en semántica
        self.semantic.declare_variable(var, expr_text)
        # Emitimos IR y Python equivalente
        self.inter.add_instruction(f"{var} = {expr_text}")
        self.pygen.add_line(f"{var} = {expr_text}", self.indent)
        return None

    # ifStatement: 'si' condition ':' statement
    def visitIfStatement(self, ctx):
        # Validar que el ID de la condición exista y que la expr sea válida
        self.visit(ctx.condition())
        cond_text = self._cond_text_from_condition(ctx.condition())
        # IR "IF ..." y línea Python "if ...:"
        self.inter.add_instruction(f"IF {cond_text}:")
        self.pygen.add_line(f"if {cond_text}:", self.indent)
        # Entramos a un bloque indentado
        self.indent += 1
        self.visit(ctx.statement())
        self.indent -= 1
        return None

    # rule_: 'si' expr ':' action  (compatibilidad con versión antigua)
    def visitRule_(self, ctx):
        # Valida IDs en la expresión condicional antigua
        self.visit(ctx.expr())
        cond_text = self._expr_text(ctx.expr())
        self.inter.add_instruction(f"IF {cond_text}:")
        self.pygen.add_line(f"if {cond_text}:", self.indent)
        self.indent += 1
        self.visit(ctx.action())
        self.indent -= 1
        return None

    # action: ID '=' expr ';' (versión antigua)
    def visitAction(self, ctx):
        # Valida IDs en el RHS de la asignación
        self.visit(ctx.expr())
        var = ctx.ID().getText()
        expr_text = self._expr_text(ctx.expr())
        self.semantic.declare_variable(var, expr_text)
        self.inter.add_instruction(f"{var} = {expr_text}")
        self.pygen.add_line(f"{var} = {expr_text}", self.indent)
        return None

    # printStatement: 'print' '(' ID ')' ';'
    def visitPrintStatement(self, ctx):
        var = ctx.ID().getText()
        # Verificación semántica: la variable debe existir
        self.semantic.check_variable(var)
        # IR y Python para imprimir
        self.inter.add_instruction(f"PRINT {var}")
        self.pygen.add_line(f"print({var})", self.indent)
        return None

    # printStmt (versión antigua)
    def visitPrintStmt(self, ctx):
        var = ctx.ID().getText()
        self.semantic.check_variable(var)
        self.inter.add_instruction(f"PRINT {var}")
        self.pygen.add_line(f"print({var})", self.indent)
        return None

    # ---- validaciones dentro de expr/condition ----
    def visitCondition(self, ctx):  # condition: ID comparator expr
        # La variable a la izquierda del comparador debe existir
        self.semantic.check_variable(ctx.ID().getText())
        # Validar recursivamente la expresión de la derecha
        self.visit(ctx.expr())
        return None

    def visitExpr(self, ctx):
        # Recorremos hijos de la expresión; si hay términos/IDs, se validarán abajo
        for ch in ctx.getChildren():
            self.visit(ch)
        return None

    def visitTerm(self, ctx):
        # term: ID | NUMBER (si existe esta regla en tu gramática)
        if hasattr(ctx, "ID") and ctx.ID() is not None:
            self.semantic.check_variable(ctx.ID().getText())
        return None


def main():
    # 1) Entrada: input.txt por defecto; si viene un argumento, usamos ese archivo
    input_file = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
    if not os.path.exists(input_file):
        print(f"❌ Error: no se encontró el archivo {input_file}")
        sys.exit(1)

    # 2) Derivar nombres por prueba (artefactos por caso) + asegurar outputs/
    base = os.path.splitext(os.path.basename(input_file))[0]
    os.makedirs("outputs", exist_ok=True)
    output_log = os.path.join("outputs", f"log_{base}.txt")
    ir_output  = os.path.join("outputs", f"ir_{base}.txt")
    py_output  = os.path.join("outputs", f"py_{base}.py")

    # Nombres clásicos en raíz (modo “como antes” para la demo rápida)
    root_log = "output.txt"
    root_ir  = "output_ir.txt"
    root_py  = "output_program.py"

    print(f"📘 Compilando: {input_file}")

    # 3) LEXER & PARSER con listeners de errores (acumulan mensajes)
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = ImpuestosLexer(input_stream)
    lexErr = CollectingErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexErr)

    tokens = CommonTokenStream(lexer)
    parser = ImpuestosParser(tokens)
    synErr = CollectingErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(synErr)

    tree = parser.program()  # nodo raíz del AST

    # 4) Si hay errores léxicos/sintácticos, registrar logs y abortar
    if lexErr.has_errors or synErr.has_errors:
        print("\n❌ Errores de análisis (léxico/sintáctico):")
        for e in (lexErr.errors + synErr.errors):
            print("  -", e)
        # Escribimos los logs tanto por caso como el clásico
        for path in (output_log, root_log):
            with open(path, "w", encoding="utf-8") as f:
                f.write("❌ Errores de análisis (léxico/sintáctico):\n")
                for e in (lexErr.errors + synErr.errors):
                    f.write(f"  - {e}\n")
        sys.exit(1)

    # 5) Fases propias: semántica + IR + Python (mediante el Visitor)
    semantic = SemanticAnalyzer()
    inter = IntermediateCode()
    pygen = PythonGenerator()

    visitor = ImpuestosCustomVisitor(semantic, inter, pygen)
    visitor.visit(tree)

    # 6) Mostrar / Guardar IR y símbolos para evidencias
    print("\n=== Tabla de Símbolos ===")
    for name, value in semantic.symbols.symbols.items():
        print(f"{name}: {value}")

    print("\n=== Código Intermedio (TAC) ===")
    inter.show()
    # Guardamos IR por caso y clásico
    inter.save_to_file(ir_output)
    inter.save_to_file(root_ir)

    # 7) Reportar semántica y, si está OK, escribir Python por caso y clásico
    if semantic.report_errors():           # True = sin errores
        # Logs por caso y clásico
        for path in (output_log, root_log):
            with open(path, "w", encoding="utf-8") as f:
                f.write("✅ Compilación completada sin errores.\n")
        # Emitir Python destino (por caso y clásico)
        pygen.write_file(py_output)
        pygen.write_file(root_py)

        print(f"✅ Archivo Python generado: {py_output}")
        print(f"✅ Archivo Python generado: {root_py}")
        print("\n🟢 Proceso completado.\n")
        sys.exit(0)
    else:
        # Si hubo errores semánticos, registrar y salir con código 1
        for path in (output_log, root_log):
            with open(path, "w", encoding="utf-8") as f:
                f.write("❌ Se encontraron errores semánticos.\n")
        print("❌ Compilación detenida por errores semánticos.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
