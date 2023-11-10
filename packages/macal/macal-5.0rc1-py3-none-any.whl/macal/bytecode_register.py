#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# This is the bytecode register.

from __future__ import annotations
import sys
from typing import Any

from .ast_nodetype import AstNodetype
from .conversion import compareTypes, typeFromValue

class BytecodeRegister:
    def __init__(self, name: str, opcode: int) -> BytecodeRegister:
        self.name: str = name                  # register name
        self.opcode: int = opcode              # register opcode, this is used in the vm to identify the register
        self.value: Any = 0
        self.type: AstNodetype = AstNodetype.INTEGER
        self._do_raise: bool = True             # raise an exception if an error occurs

    def reset(self) -> None:
        self.type = AstNodetype.INTEGER
        self.value = 0

    def error(self, message: str) -> None:
        msg = f"Register Error: {message}"
        if self._do_raise:
            raise Exception(msg)
        print(msg)
        sys.exit(1)


    def __str__(self) -> str:
        return f"{self.name} {self.type.name} {self.value} {self.opcode}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: BytecodeRegister) -> BytecodeRegister:
        self.value = self.type == other.type and self.value == other.value
        self.type = AstNodetype.BOOLEAN
        return self

    def __ne__(self, other: BytecodeRegister) -> BytecodeRegister:
        self.value = self.type != other.type or self.value != other.value
        self.type = AstNodetype.BOOLEAN
        return self

    def __lt__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.type != other.type:
            self.error(f"Cannot compare {self.type} with {other.type}")
        self.value = self.value < other.value
        self.type = AstNodetype.BOOLEAN
        return self

    def __le__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.type != other.type:
            self.error(f"Cannot compare {self.type} with {other.type}")
        self.value = self.value <= other.value
        self.type = AstNodetype.BOOLEAN
        return self

    def __gt__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.type != other.type:
            self.error(f"Cannot compare {self.type} with {other.type}")
        self.value = self.value > other.value
        self.type = AstNodetype.BOOLEAN
        return self

    def __ge__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.type != other.type:
            self.error(f"Cannot compare {self.type} with {other.type}")
        self.value = self.value >= other.value
        self.type = AstNodetype.BOOLEAN
        return self

    def __expand_to_float__(self, other: BytecodeRegister) -> bool:
        # expand to float if one of the types is float.
        if ((self.type == AstNodetype.FLOAT or other.type == AstNodetype.FLOAT) and
           (self.type == AstNodetype.INTEGER or other.type == AstNodetype.INTEGER)):
            self.type = AstNodetype.FLOAT
            self.value = float(self.value)
            other.value = float(other.value)
            return True
        return False

    def __expand_to_string__(self, other: BytecodeRegister) -> bool:
        if (self.type in (AstNodetype.STRING,
                          AstNodetype.STRING_INTERPOLATION_STRING_PART,
                          AstNodetype.STRING_INTERPOLATION_END)
                          or other.type in
                          (AstNodetype.STRING,
                           AstNodetype.STRING_INTERPOLATION_STRING_PART,
                           AstNodetype.STRING_INTERPOLATION_END)):
            self.type = AstNodetype.STRING
            self.value = str(self.value)
            other.value = str(other.value)
            return True
        return False

    def __add__(self, other: BytecodeRegister) -> BytecodeRegister:
        if not compareTypes(self.type, other.type):
            if not (self.__expand_to_float__(other) or self.__expand_to_string__(other)):
                self.error(f"Cannot add {self.type} with {other.type}")
        self.value += other.value
        return self

    def __sub__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.type != other.type:
            if not self.__expand_to_float__(other):
                self.error(f"Cannot subtract {self.type} with {other.type}")
        self.value -= other.value
        return self

    def __mul__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.type != other.type:
            if not self.__expand_to_float__(other):
                self.error(f"Cannot multiply {self.type} with {other.type}")
        self.value *= other.value
        return self

    def __truediv__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.type != other.type:
            if not self.__expand_to_float__(other):
                self.error(f"Cannot divide {self.type} with {other.type}")
        self.value /= other.value
        self.type = typeFromValue(self.value)
        return self

    def __mod__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.type != other.type:
            if not self.__expand_to_float__(other):
                self.error(f"Cannot modulus {self.type} with {other.type}")
        self.value %= other.value
        return self

    def __pow__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.type != other.type:
            if not self.__expand_to_float__(other):
                self.error(f"Cannot power {self.type} with {other.type}")
        self.value **= other.value
        return self

    def __and__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.type != other.type:
            self.error(f"Cannot AND {self.type} with {other.type}")
        self.value = self.value and other.value
        self.type = AstNodetype.BOOLEAN
        return self

    def __or__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.type != other.type:
            self.error(f"Cannot OR {self.type} with {other.type}")
        self.value = self.value or other.value
        self.type = AstNodetype.BOOLEAN
        return self

    def __xor__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.type != other.type:
            self.error(f"Cannot XOR {self.type} with {other.type}")
        if self.name == other.name:
            self.value = int(0)
            self.type = AstNodetype.INTEGER
            return self
        self.value = self.value ^ other.value
        return self

    def __bool__(self) -> BytecodeRegister:
        if self.type != AstNodetype.BOOLEAN:
            self.error(f"Cannot invert {self.type}")
        self.value = not self.value
        return self

    def __neg__(self) -> BytecodeRegister:
        if self.type != AstNodetype.INTEGER and self.type != AstNodetype.FLOAT:
            self.error(f"Cannot negate {self.type}")
        self.value = -self.value
        return self

    def fromRegister(self, register: BytecodeRegister) -> None:
        self.type = register.type
        self.value = register.value

    def set(self, type: AstNodetype, value: Any) -> None:
        self.type = type
        self.value = value

