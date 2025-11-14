# Estructura mínima de una tabla de símbolos para el compilador
class SymbolTable:
    def __init__(self):
        # Diccionario: nombre_de_variable -> valor (opcional)
        self.symbols = {}

    def define(self, name, value=None):
        # Declara/actualiza una variable en la tabla
        self.symbols[name] = value

    def exists(self, name):
        # Indica si la variable ya fue declarada
        return name in self.symbols

    def get(self, name):
        # Obtiene el valor asociado (o None si no existe/ no tiene valor)
        return self.symbols.get(name, None)
