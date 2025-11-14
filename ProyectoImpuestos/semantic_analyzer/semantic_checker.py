from semantic_analyzer.symbols_table import SymbolTable

# Analizador semántico: verifica reglas de significado del programa
class SemanticAnalyzer:
    def __init__(self):
        # Tabla de símbolos (variables conocidas y, opcionalmente, su valor)
        self.symbols = SymbolTable()
        # Acumula mensajes de error semántico encontrados
        self.errors = []

    def declare_variable(self, name, value=None):
        # Registra/declara una variable en la tabla de símbolos
        self.symbols.define(name, value)

    def check_variable(self, name):
        # Verifica uso de variable: debe existir previamente en la tabla
        if not self.symbols.exists(name):
            self.errors.append(f"Error semántico: variable '{name}' no declarada.")

    def show_symbol_table(self):
        # Muestra la tabla de símbolos en consola (evidencia de la fase semántica)
        print("=== Tabla de Símbolos ===")
        for name, value in self.symbols.symbols.items():
            print(f"{name}: {value}")

    def report_errors(self):
        # Reporta y resume el resultado del análisis semántico
        if self.errors:
            print("❌ Se encontraron errores semánticos:")
            for e in self.errors:
                print("  -", e)
            return False  # hubo errores
        else:
            print("✅ Análisis semántico exitoso.")
            return True   # sin errores

