#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# Interactive Line Interpreter class

from .macal_lexer import Lexer
from .macal_parser import Parser
from .macal_compiler import MacalCompiler
from .__about__ import __version__, __author__, __author_email__, __license__, __copyright__

class MacalInteractive:
    def __init__(self) -> None:
        self.lexer = Lexer()
        self.parser = Parser()
        self.compiler = MacalCompiler()

    def ReadLine(self) -> str:
        return input(">>> ")

    def ExecuteLine(self, text: str) -> None:
        tokens = self.lexer.lex(text)
        print(tokens)
        ast = self.parser.parse_interactive(tokens)
        print(ast)
        start = self.compiler.cs.rip.value
        self.compiler.cs.flags.trap = True
        self.compiler.compile_interactive(ast)
        end = self.compiler.cs.rip.value
        self.compiler.cs.rip.value = start
        while self.compiler.cs.rip.value < end:
            self.compiler.cs.Execute()
            self.compiler.cs.Halted = False
        self.compiler.cs.flags.trap = False

    def Run(self) -> None:
        print("Macal Interactive Interpreter v" + __version__)
        print("Type 'exit' to exit. Type 'copyright', 'credits' or 'license' for more information.")
        while True:
            try:
                text = self.ReadLine()
                if text is None or text.strip() == "":
                    continue
                if text == "exit":
                    break
                if text == "credits":
                    print("Product:   Macal")
                    print("Author:    ", __author__)
                    print("Email:     ", __author_email__)
                elif text == "license":
                    print("License:   ", __license__)
                elif text == "copyright":
                    print("Copyright:   ", __copyright__)
                else:
                    self.ExecuteLine(text.strip())
            except Exception as e:
                print(e)
                continue
    