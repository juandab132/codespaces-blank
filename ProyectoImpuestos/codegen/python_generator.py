# Generador de código Python a partir del IR/visita del AST
class PythonGenerator:
    def __init__(self):
        # Acumula líneas de código Python ya formateadas
        self.lines = []

    def add_line(self, line, indent=0):
        # Agrega una línea con la indentación indicada (4 espacios por nivel)
        self.lines.append("    " * indent + line)

    def write_file(self, filename="output_program.py"):
        # Escribe todas las líneas acumuladas en un archivo .py
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(self.lines))
        # Mensaje de confirmación para la demo
        print(f"✅ Archivo Python generado: {filename}")
