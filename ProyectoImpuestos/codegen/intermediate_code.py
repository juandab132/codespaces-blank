# Clase responsable de construir y almacenar el Código Intermedio (IR/TAC)
class IntermediateCode:
    def __init__(self):
        # Lista donde guardamos, en orden, cada instrucción TAC como texto
        self.instructions = []

    def add_instruction(self, code):
        # Agrega una instrucción al IR (por ejemplo: "x = 5", "IF cond:", "PRINT x")
        self.instructions.append(code)

    def show(self):
        # Muestra el IR en consola, numerando cada instrucción para facilitar la lectura
        print("=== Código Intermedio ===")
        for i, inst in enumerate(self.instructions, start=1):
            print(f"{i}: {inst}")

    def save_to_file(self, filename="output_ir.txt"):
        # Guarda el IR numerado en un archivo de texto (por defecto: output_ir.txt)
        with open(filename, "w") as f:
            for i, inst in enumerate(self.instructions, start=1):
                f.write(f"{i}: {inst}\n")

