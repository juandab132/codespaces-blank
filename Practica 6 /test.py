import sys
from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser

def main():
    
    input_stream = InputStream("SELECT nombre, edad FROM usuarios WHERE edad >= 18;")
    
    # Lexer (tokens)
    lexer = MiGramaticaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    
    
    token_stream.fill()
    print("📌 TOKENS:")
    for token in token_stream.getTokens():
        print(token)

    
    parser = MiGramaticaParser(token_stream)
    tree = parser.query()

    print("\n📌 Árbol sintáctico:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
