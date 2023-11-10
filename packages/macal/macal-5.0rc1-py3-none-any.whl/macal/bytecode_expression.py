#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# This is the bytecode expression.

from __future__ import annotations
from .ast_nodetype import AstNodetype

class BytecodeExpression:
    def __init__(self, type: AstNodetype, line: int, column: int) -> BytecodeExpression:
        self.type: AstNodetype = type
        self.line: int = line
        self.column: int = column

    def __str__(self) -> str:
        return f"{self.type} {self.line} {self.column}"

    def __repr__(self) -> str:
        return self.__str__()