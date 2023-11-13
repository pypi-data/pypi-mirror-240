#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#


from typing import List, Any
from .bytecode_register import BytecodeRegister

class BytecodeFlagsRegister(BytecodeRegister):
    def __init__(self, name: str, opcode: int) -> BytecodeRegister:
        super().__init__(name, opcode)
        self._carry: bool = False
        self._zero: bool = False
        self._sign: bool = False
        self._overflow: bool = False
        self._direction: bool = False
        self._interrupt: bool = False
        self._trap: bool = False
        self._supervisor: bool = False
        self._negative: bool = False
        self._index: bool = False

    def __str__(self) -> str:
        self._set_bit(6, self._zero)
        self._set_bit(0, self._carry)
        return f"CF {self._get_bit(0)} PF {self._get_bit(2)} ZF {self._get_bit(6)} SF {self._get_bit(7)} TF {self._get_bit(8)} DF {self._get_bit(10)} OF {self._get_bit(11)} IDX {self._get_bit(32)}"

    def _get_bit(self, bit: int) -> str:
        return '1' if (self.value & (1 << bit)) != 0 else '0'

    def __repr__(self) -> str:
        return self.__str__()

    def clear(self) -> None:
        self._carry = False # bit 0 (status)
        self._set_bit(1, True) # bit 1 is always true in EFLAGS
        self._parity = False # bit 2 (status)
        # bit 3 is reserved
        #self._auxiliary_carry = False # bit 4 (status)
        # bit 5 is reserved
        self._zero = False # bit 6 (status)
        self._sign = False # bit 7 (status)
        self._trap = False # bit 8 (single step) (control)
        #self._interrupt = False # bit 9 (interrupt enable) (control)
        self._direction = False # bit 10 (direction) (control)
        self._overflow = False # bit 11 (overflow) (status)
        self._index = False # bit 32 (status) (not a real flag, but used as such for the time being)
        # for RFLAGS bits 32-63 are reserved and must be 0

    def _set_bit(self, bit: int, value: bool) -> None:
        if value:
            self.value |= (1 << bit)
        else:
            self.value &= ~(1 << bit)

    @property
    def carry(self) -> bool:
        return self._carry

    @carry.setter
    def carry(self, value: bool) -> None:
        self._carry = value
        self._set_bit(0, value)

    @property
    def parity(self) -> bool:
        return self._parity

    @parity.setter
    def parity(self, value: bool) -> None:
        self._parity = value
        self._set_bit(2, value)

    @property
    def zero(self) -> bool:
        return self._zero

    @zero.setter
    def zero(self, value: bool) -> None:
        self._zero = value
        self._set_bit(6, value)

    @property
    def sign(self) -> bool:
        return self._sign

    @sign.setter
    def sign(self, value: bool) -> None:
        self._sign = value
        self._set_bit(7, value)

    @property
    def trap(self) -> bool:
        return self._trap

    @trap.setter
    def trap(self, value: bool) -> None:
        self._trap = value
        self._set_bit(8, value)

    @property
    def direction(self) -> bool:
        return self._direction

    @direction.setter
    def direction(self, value: bool) -> None:
        self._direction = value
        self._set_bit(10, value)

    @property
    def overflow(self) -> bool:
        return self._overflow

    @overflow.setter
    def overflow(self, value: bool) -> None:
        self._overflow = value
        self._set_bit(11, value)

    @property
    def index(self) -> bool:
        return self._index

    @index.setter
    def index(self, value: bool) -> None:
        self._index = value
        self._set_bit(32, value)

    def reset(self) -> None:
        self.clear()