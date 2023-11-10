#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# This is the bytcode compiler for Macal 2

from __future__ import annotations
import sys
import os
from typing import List, Optional
from .ast_nodetype import AstNodetype
from .ast_node_statement import AstNodeStatement
from .ast_node_expression import AstNodeExpression
from .ast_node_binary_expression import AstNodeBinaryExpression
from .ast_node_unary_expression import AstNodeUnaryExpression
from .ast_node_literal_expression import AstNodeLiteralExpression
from .ast_node_program import AstNodeProgram
from .ast_node_block import AstNodeBlock
from .ast_node_if_statement import AstNodeIfStatement
from .ast_node_elif_statement import AstNodeElifStatement
from .ast_node_else_statement import AstNodeElseStatement
from .ast_node_assignment import AstNodeAssignmentStatement
from .ast_node_indexed_variable_expression import AstNodeIndexedVariableExpression
from .ast_node_function_call_expression import AstNodeFunctionCallExpression
from .ast_node_variable_expression import AstNodeVariableExpression
from .ast_node_variable_function_call_expression import AstNodeVariableFunctionCallExpression
from .ast_node_print_statement import AstNodePrintStatement
from .ast_node_break_statement import AstNodeBreakStatement
from .ast_node_continue_statement import AstNodeContinueStatement
from .ast_node_return_statement import AstNodeReturnStatement
from .ast_node_halt_statement import AstNodeHaltStatement
from .ast_node_library_expression import AstNodeLibraryExpression
from .ast_node_include_statement import AstNodeIncludeStatement
from .ast_node_while_statement import AstNodeWhileStatement
from .ast_node_foreach_statement import AstNodeForeachStatement
from .ast_node_function_definition import AstNodeFunctionDefinition
from .ast_node_function_call_statement import AstNodeFunctionCallStatement
from .ast_node_function_parameter import AstNodeFunctionParameter
from .ast_node_type_statement import AstNodeTypeStatement
from .ast_node_istype import AstNodeIsType
from .macal_vm import MacalVm
from .macal_instructions import Opcode
from .bytecode_optimizer import BytecodeOptimizer
from .compiler_scope import CompilerScope
from .bytecode_register import BytecodeRegister
from .ct_function import CTFunction
from .ct_variable import CTVariable
from .lex_token import LexToken
from .macal_select_compiler import MacalSelectCompiler
from .macal_lexer import Lexer
from .macal_parser import Parser
from .switch_case_table import SwitchCaseTable
from .config import SearchPath

# Function stack layout:

# -6 PARAMETER 0
# -5 PARAMETER 1
# -4 PARAMCOUNT
# -3 RETURN VALUE
# -2 RETURN ADDRESS
# -1 RBP

FUNCTION_CALL_PARAMETER_STACK_OFFSET = -5
FUNCTION_CALL_PARAMETER_COUNT_STACK_OFFSET = -4
FUNCTION_CALL_RETURN_VALUE_STACK_OFFSET = -3
FUNCTION_CALL_RETURN_ADDRESS_STACK_OFFSET = -2
FUNCTION_CALL_PREVIOUS_RBP_STACK_OFFSET = -1

class MacalCompiler:
    def __init__(self, program: Optional[AstNodeProgram] = None, output_path: Optional[str] = None, verbose: bool = False, debug: bool = False) -> MacalCompiler:
        self.program: Optional[AstNodeProgram] = program
        self.output_path: Optional[str] = output_path
        self.output_file: Optional[str] = None
        self.cs: MacalVm = MacalVm() # Code segment
        self.scope: CompilerScope = CompilerScope("global", None)
        self.do_raise: bool = True
        self.debug = debug
        compiler_path = os.path.dirname(__file__)
        lib_path = os.path.join(compiler_path, "lib")
        if lib_path not in SearchPath:
            SearchPath.append(lib_path)
        if compiler_path not in SearchPath:
            SearchPath.append(compiler_path)
        self.verbose: bool = verbose

    def error(self, message: str) -> None:
        msg = f"Compiler Error: {message}"
        if self.do_raise:
            raise Exception(msg)
        print(msg)
        sys.exit(1)

    def compile(self) -> None:
        self.cs.Reset()
        # we need to start at an offset of 2 because exit code
        # and return address zero are on the stack and not to be touched.
        self.cs.rsp.value = 2
        self.cs.rbp.value = 2
        self.compile_program(self.program, self.scope)
        self.__resolve_jumps_and_labels__(self.scope)
        #opt = BytecodeOptimizer(self.cs, self.scope)
        #opt.process()
        if self.verbose:
            self.compile_datasegment(self.scope)
        self.cs.Save(self.output_path, self.cs.rip.value)

    def compile_interactive(self, ast: AstNodeProgram) -> None:
        self.compile_program(ast, self.scope)
        self.__resolve_jumps_and_labels__(self.scope)
        if self.verbose:
            self.compile_datasegment(self.scope)

    def __resolve_jumps_and_labels__(self, scope: CompilerScope) -> None:
        for jump in scope.jump_table:
            jaddr: int = jump.address
            laddr: int = scope.labels[jump.label].address
            op = self.cs.memory[jaddr]
            new_op = (op[0], laddr)
            self.cs.memory[jaddr] = new_op

        for switch_case_table in scope.switch_jump_tables:
            for case, label in switch_case_table.labels.items():
                laddr: int = scope.labels[label].address
                switch_case_table.labels[case] = laddr

            op = self.cs.memory[switch_case_table.address]
            new_op = (op[0], op[1], op[2], switch_case_table.labels)
            self.cs.memory[switch_case_table.address] = new_op

    def compile_program(self, program: AstNodeProgram, scope: CompilerScope) -> None:
        label_main = self.scope.get_new_label("main")
        label_exit = self.scope.get_new_label("exit")
        self.scope.set_label_address(label_main, self.cs.rip.value)
        main_scope = self.emit_scope(scope)
        self.compile_block(program, scope)
        self.scope.set_label_address(label_exit, self.cs.rip.value)
        self.emit_scope_end(main_scope)
        self.cs.Emit_RET()

    def compile_block(self, block: AstNodeBlock, scope: CompilerScope) -> None:
        for statement in block.statements:
            self.compile_statement(statement, scope)

    def compile_statement(self, statement: AstNodeStatement, scope: CompilerScope) -> None:
        if statement.type == AstNodetype.IF_STATEMENT:
            self.compile_if_statement(statement, scope)
        elif statement.type == AstNodetype.FOREACH_STATEMENT:
            self.compile_foreach_statement(statement, scope)
        elif statement.type == AstNodetype.WHILE_STATEMENT:
            self.compile_while_statement(statement, scope)
        elif statement.type == AstNodetype.CONTINUE_STATEMENT:
            self.compile_continue_statement(statement, scope)
        elif statement.type == AstNodetype.BREAK_STATEMENT:
            self.compile_break_statement(statement, scope)
        elif statement.type == AstNodetype.RETURN_STATEMENT:
            self.compile_return_statement(statement, scope)
        elif statement.type == AstNodetype.SELECT_STATEMENT:
            self.compile_select_statement(statement, scope)
        elif statement.type == AstNodetype.HALT_STATEMENT:
            self.compile_halt_statement(statement, scope)
        elif statement.type == AstNodetype.INCLUDE_STATEMENT:
            self.compile_include_statement(statement, scope)
        elif statement.type == AstNodetype.PRINT_STATEMENT:
            self.compile_print_statement(statement, scope)
        elif statement.type == AstNodetype.SWITCH_STATEMENT:
            self.compile_switch_statement(statement, scope)
        elif statement.type == AstNodetype.ASSIGNMENT_STATEMENT:
            self.compile_assignment_statement(statement, scope)
        elif statement.type == AstNodetype.FUNCTION_CALL:
            self.compile_function_call(statement, scope)
        elif statement.type == AstNodetype.FUNCTION_DEFINITION:
            self.compile_function_definition(statement, scope)
        elif statement.type == AstNodetype.FUNCTION_CALL_EXPRESSION:
            self.compile_function_call_expression(statement, scope)
        else:
            self.error(f"Unknown statement type {statement.type} at {statement.line}:{statement.column} scope({scope.name})")

# code writing helpers.

    def new_child_scope(self, name: str, scope: CompilerScope,
                        lbl_continue: Optional[int] = None,
                        lbl_end: Optional[int] = None ) -> CompilerScope:
        child = scope.new_child(name)
        child.continue_label = lbl_continue
        child.break_label = lbl_end
        child.rbp_offset = scope.rbp_offset

    def emit_compare_condition_and_jump_if_not_zero(self, label: int, scope: CompilerScope) -> None:
        self.emit_condition(label, Opcode.JMPNZ, scope)

    def emit_condition(self, label: int, conditional_jump: int, scope: CompilerScope) -> None:
        self.emit_pop(self.cs.rax)                                # pop rax
        self.cs.Emit_CMPRI(self.cs.rax, AstNodetype.BOOLEAN, True)   # cmpir rax, True
        self.emit_jump(conditional_jump, label, scope)   # jmpnz label

    def get_new_label(self, name: str, scope: CompilerScope) -> int:
        return scope.root.get_new_label(name)

    def emit_new_label(self, name: str, scope: CompilerScope) -> int:
        lbl = scope.root.get_new_label(name)
        scope.root.set_label_address(lbl, self.cs.rip.value)
        return lbl

    def emit_label(self, label: int, scope: CompilerScope) -> None:
        scope.set_label_address(label, self.cs.rip.value)

    def emit_push(self, reg: BytecodeRegister) -> None:
        self.cs.Emit_PUSH(reg)
        self.cs.rsp.value += 1

    def emit_pop(self, reg: BytecodeRegister) -> None:
        self.cs.Emit_POP(reg)
        self.cs.rsp.value -= 1

    def emit_movrr(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.cs.Emit_MOVRR(reg1, reg2)
        if reg1.name == 'RBP' and reg2.name == 'RSP':
            self.cs.rbp.value = self.cs.rsp.value
        elif reg1.name == 'RSP' and reg2.name == 'RBP':
            self.cs.rsp.value = self.cs.rbp.value

    def emit_scope(self, scope: CompilerScope) -> CompilerScope:
        self.emit_push(self.cs.rbp)
        self.emit_movrr(self.cs.rbp, self.cs.rsp)
        child: CompilerScope = scope.new_child(f"scope", self.cs.rbp.value)
        return child

    def emit_scope_end(self, scope: CompilerScope) -> None:
        self.emit_movrr(self.cs.rsp, self.cs.rbp)
        self.emit_pop(self.cs.rbp)
        scope.discard()

    def emit_stor(self, offset: int, reg: BytecodeRegister) -> None:
        self.cs.Emit_STOR(offset, reg)

    def emit_storr(self, offset: int, reg: BytecodeRegister) -> None:
        self.cs.Emit_STORR(self.cs.rbp, offset, reg)

    def emit_load(self, reg: BytecodeRegister, offset: int) -> None:
        self.cs.Emit_LOAD(reg, offset)

    def emit_loadr(self, reg: BytecodeRegister, offset: int) -> None:
        self.cs.Emit_LOADR(reg, self.cs.rbp, offset)

    def emit_jump(self, opcode: int, label: int, scope: CompilerScope) -> None:
        if label is None:
            self.error(f"Label is None at {self.cs.rip.value}")
        scope.root.new_jump(self.cs.rip.value, label)
        if opcode == Opcode.JMP: self.cs.Emit_JMP(label)
        elif opcode == Opcode.JMPZ: self.cs.Emit_JMPZ(label)
        elif opcode == Opcode.JMPNZ: self.cs.Emit_JMPNZ(label)
        elif opcode == Opcode.JMPGT: self.cs.Emit_JMPGT(label)
        elif opcode == Opcode.JMPGTE: self.cs.Emit_JMPGTE(label)
        elif opcode == Opcode.JMPLT: self.cs.Emit_JMPLT(label)
        elif opcode == Opcode.JMPLTE: self.cs.Emit_JMPLTE(label)
        elif opcode == Opcode.DJNZ: self.cs.Emit_DJNZ(label)
        else: self.error(f"Unknown jump opcode {opcode} at {self.cs.rip.value}")

    def emit_jump_table(self, jump_table: dict, scope: CompilerScope) -> None:
        scope.switch_jump_tables.append(SwitchCaseTable(self.cs.rip.value, jump_table))

    def emit_call(self, address: int) -> None:
        self.cs.Emit_CALL(address)
        self.cs.rsp.value += 1 # reserve space for the return value.

    def emit_callr(self, reg: BytecodeRegister) -> None:
        if reg.name == "RAX":
            self.error("Can't use RAX in CALL/CALLR, RAX is reset to push a placeholder for the return value on the stack.")
        self.cs.Emit_CALLR(reg)
        self.cs.rsp.value += 1 # reserve space for the return value.

# expression helper functions.

    def var_to_stack(self, var: CTVariable) -> None:
        if var.scope.is_function_definition:
            self.emit_loadr(self.cs.rax, var.stack_offset)
        else:
            self.emit_load(self.cs.rax, var.stack_offset)
        self.emit_push(self.cs.rax)                     # push rax

# compiling statements

    def compile_if_statement(self, statement: AstNodeIfStatement, scope: CompilerScope) -> None:
        self.emit_new_label("if", scope)
        self.compile_expression(statement.condition, scope)
        label_at_the_very_end_of_if = scope.get_new_label("label_end")
        label_for_JMPNZ_in_if = scope.get_new_label("label_jnz")
        self.emit_compare_condition_and_jump_if_not_zero(label_for_JMPNZ_in_if, scope)
        self.compile_block(statement.block, scope)
        self.emit_jump(Opcode.JMP, label_at_the_very_end_of_if, scope)
        self.emit_label(label_for_JMPNZ_in_if, scope)
        if statement.elif_block_list is not None:
            count = len(statement.elif_block_list)
            if count > 0:
                for elif_statement in statement.elif_block_list:
                    self.compile_elif_statement(elif_statement, label_at_the_very_end_of_if, scope)
        if statement.else_block is not None and len(statement.else_block.statements) > 0:
            self.compile_else_statement(statement.else_block, scope)
        self.emit_label(label_at_the_very_end_of_if, scope)

    def compile_elif_statement(self, statement: AstNodeElifStatement, lbl_end: int, scope: CompilerScope) -> None:
        self.emit_new_label("elif", scope)
        self.compile_expression(statement.condition, scope)
        label = self.get_new_label("elif_jnz", scope)
        self.emit_compare_condition_and_jump_if_not_zero(label, scope)
        self.compile_block(statement.statements, scope)
        self.emit_jump(Opcode.JMP, lbl_end, scope)
        scope.set_label_address(label, self.cs.rip.value)
        self.emit_new_label("/elif", scope)

    def compile_else_statement(self, statement: AstNodeElseStatement, scope: CompilerScope) -> None:
        self.emit_new_label("else", scope)
        self.compile_block(statement, scope)
        self.emit_new_label("/else", scope)

    def compile_foreach_statement(self, statement: AstNodeForeachStatement, scope: CompilerScope) -> None:
        foreach_end_label = self.get_new_label("foreach_loop_end", scope)
        self.emit_new_label("foreach_start", scope)
        foreach_continue_label = scope.get_new_label("foreach_loop_continue")
        foreach_scope = self.emit_scope(scope)
        # get the variable we are iterating over
        self.compile_expression(statement.expr, foreach_scope)  # array is on stack [rbp + 0]
        self.cs.Emit_LEN(self.cs.rax)                              # len rax
        self.emit_push(self.cs.rax)                             # push length       [rbp + 1]
        self.cs.Emit_XOR(self.cs.rax, self.cs.rax) # xor rax, rax
        self.emit_push(self.cs.rax)                             # push index        [rbp + 2]
        it = foreach_scope.define_variable("it", self.cs.rsp.value)
        it.type = AstNodetype.INTEGER
        it.value = 0
        self.emit_push(self.cs.rax)                             # push variable it  [rbp + 3]
        # preparation is done, we can start the loop:
        foreach_loop_start = self.emit_new_label("foreach_loop_start", scope)
        foreach_scope.continue_label = foreach_continue_label
        foreach_scope.break_label = foreach_end_label
        self.emit_load(self.cs.rax, 1 + foreach_scope.rbp_offset)                # load rax, [rbp + 1] # rax is now the length
        self.emit_load(self.cs.rbx, 2 + foreach_scope.rbp_offset)                # load rbx, [rbp + 2] # rbx is now index
        self.cs.Emit_CMPRR(self.cs.rax, self.cs.rbx)       # cmprr rax, rbx
        self.emit_jump(Opcode.JMPZ, foreach_end_label, scope.root) # jmpz foreach_end_label if rax == rbx (we are at the end of the array)
        self.emit_load(self.cs.rax, 0 + foreach_scope.rbp_offset)                # load rax, [rbp + 0] # rax is now the array
        self.cs.Emit_FEINDEX()              # rax = rax[rbx]      # rax is now the value for the variable it
        self.emit_stor(it.stack_offset, self.cs.rax)                # it is now the value of the array at the current index
        self.compile_block(statement.block, foreach_scope) # compile the block of the foreach statement.
        self.emit_label(foreach_continue_label, scope)
        self.emit_load(self.cs.rax, 2 + foreach_scope.rbp_offset)                # load rax, [rbp + 2] # rax is now the index
        self.cs.Emit_INC(self.cs.rax)                      # inc rax rax = rax + 1
        self.emit_stor(2 + foreach_scope.rbp_offset, self.cs.rax)                # stor [rbp + 2], rax increased the index
        self.emit_jump(Opcode.JMP, foreach_loop_start, scope)
        self.emit_label(foreach_end_label, scope)
        self.emit_scope_end(foreach_scope)
        self.emit_new_label("foreach_end", scope)

    def compile_while_statement(self, statement: AstNodeWhileStatement, scope: CompilerScope) -> None:
        self.emit_new_label("while", scope)
        loop_start = self.get_new_label("while_loop_start", scope)
        loop_end   = self.get_new_label("while_loop_end", scope)
        while_scope = self.emit_scope(scope)
        while_scope.continue_label = loop_start
        while_scope.break_label = loop_end
        self.emit_label(loop_start, scope)
        self.compile_expression(statement.condition, scope)
        self.emit_compare_condition_and_jump_if_not_zero(loop_end, scope)
        self.compile_block(statement.block, while_scope)
        self.emit_jump(Opcode.JMP, loop_start, scope)
        self.emit_label(loop_end, scope)
        self.emit_scope_end(while_scope)

    def compile_continue_statement(self, statement: AstNodeContinueStatement, scope: CompilerScope) -> None:
        if scope.continue_label is None:
            self.error(f"Continue statement not allowed at {statement.line}:{statement.column}")
        self.emit_new_label("continue", scope)
        self.emit_jump(Opcode.JMP, scope.continue_label, scope)

    def compile_break_statement(self, statement: AstNodeBreakStatement, scope: CompilerScope) -> None:
        if scope.break_label is None:
            self.error(f"Break statement not allowed at {statement.line}:{statement.column}")
        self.emit_new_label("break", scope)
        self.emit_jump(Opcode.JMP, scope.break_label, scope)

    def compile_return_statement(self, statement: AstNodeReturnStatement, scope: CompilerScope) -> None:
        if scope.exit_label is None:
            self.error(f"Return statement not allowed at {statement.line}:{statement.column}")
        self.emit_new_label("return", scope)
        if statement.expr is not None:
            self.compile_expression(statement.expr, scope)
            # the function return value is reserved at [rbp - 2]
            self.emit_pop(self.cs.rax)                   # pop rax
            self.emit_storr(-3, self.cs.rax)            # storr [rbp - 3], rax
        # jump to the exit label, the cleanup and the RET are executed there.
        self.emit_jump(Opcode.JMP, scope.exit_label, scope)

    def compile_select_statement(self, statement: AstNodeStatement, scope: CompilerScope) -> None:
        sc = MacalSelectCompiler(self)
        sc.compile_select(statement, scope)

    def compile_halt_statement(self, statement: AstNodeHaltStatement, scope: CompilerScope) -> None:
        self.emit_new_label("halt", scope)
        self.compile_expression(statement.expr, scope)
        self.emit_pop(self.cs.rax)              # pop rax
        self.emit_stor(0, self.cs.rax)       # stor [0], rax -> rax is the exit code
        self.cs.Emit_HALT()

    def compile_print_statement(self, statement: AstNodePrintStatement, scope: CompilerScope) -> None:
        self.emit_new_label("print", scope)
        for expr in statement.args:
            self.compile_expression(expr, scope)
            self.emit_pop(self.cs.rax)              # pop rax
            self.cs.Emit_PRNT()
        self.cs.Emit_MOVRI(self.cs.rax, AstNodetype.STRING, "\n")
        self.cs.Emit_PRNT()

    def compile_switch_statement(self, statement: AstNodeStatement, scope: CompilerScope) -> None:
        # A switch statement is basically a jump table.
        # So we need to compile the expression and then jump to the correct label.
        # If there is no match, we jump to the default label.
        switch_end_label = self.get_new_label("switch_end", scope)
        default_label = self.get_new_label("switch_default", scope)

        self.emit_new_label("switch", scope)
        self.compile_expression(statement.expr, scope)
        # The expression result is on the stack now this is the value that we need to match

        # Against each of the case values.
        # So first we build the jump table:
        jump_table = {}
        for case in statement.cases:
            case_label = self.get_new_label("case", scope)
            jump_table[case.case_value()] = case_label

        # Now we can compile the jump table.
        self.emit_jump_table(jump_table, scope)
        self.cs.Emit_MOVRI(self.cs.rax, AstNodetype.RECORD, jump_table)

        # Now we calculate which jump to make.
        self.emit_pop(self.cs.rbx)              # pop rbx # rbx is the value to match
        self.cs.Emit_HASFLDRR(self.cs.rax, self.cs.rbx) # hasfldrr rax, rbx. The ZF flag is set if the value is found.
        self.emit_jump(Opcode.JMPNZ, default_label, scope) # jmpz default_label if the value is not found.
        self.cs.Emit_INDEX()
        self.cs.Emit_JMPR(self.cs.rax) # jmp rax
        self.emit_label(default_label, scope)
        if statement.default is not None:
            self.compile_block(statement.default.block, scope)
        self.emit_jump(Opcode.JMP, switch_end_label, scope)
        for case in statement.cases:
            self.emit_label(jump_table[case.case_value()], scope)
            self.compile_block(case.block, scope)
            self.emit_jump(Opcode.JMP, switch_end_label, scope)
        self.emit_label(switch_end_label, scope)

    def compile_is_type_statement(self, statement: AstNodeIsType, scope: CompilerScope) -> None:
        # This should cover all the IsXXXX type statements.
        self.emit_new_label("is_type", scope)
        self.compile_expression(statement.expr, scope)
        self.emit_pop(self.cs.rax)              # pop rax
        self.cs.Emit_CMPRTI(self.cs.rax, statement.TypeToCheck)
        self.cs.Emit_SETZR(self.cs.rax)
        self.emit_push(self.cs.rax)              # push rax

    def compile_type_statement(self, statement: AstNodeTypeStatement, scope: CompilerScope) -> None:
        self.emit_new_label("Type", scope)
        self.compile_expression(statement.expr, scope)
        self.emit_pop(self.cs.rax)              # pop rax
        self.cs.Emit_TYPE(self.cs.rax)
        self.emit_push(self.cs.rax)              # push rax

    def compile_assignment_statement(self, statement: AstNodeAssignmentStatement, scope: CompilerScope) -> None:
        # Assignment works almost like a binary expression.
        # We are assured that the lhs is a variable.
        # The RHS can be anything.
        self.emit_new_label("assign", scope)
        var = scope.get_variable(statement.name)
        is_new_var = False
        if var is None: # we go assign a new var.
            var = scope.define_variable(statement.name,self.cs.rsp.value)
            var.const = statement.const
            self.cs.Emit_XOR(self.cs.rax, self.cs.rax) # xor rax, rax rax = 0
            self.emit_push(self.cs.rax)             # push rax reserve the variable on the stack.
            is_new_var = True
        if var.const and not is_new_var:
            self.error(f"Cannot assign to const {statement.name} at {statement.line}:{statement.column} scope({scope.name})")
        if not isinstance(var, CTVariable):
            self.error(f"Cannot assign to function {statement.name} at {statement.line}:{statement.column} scope({scope.name})")
        if statement.lhs.type == AstNodetype.INDEXED_VARIABLE_EXPRESSION:
            if is_new_var:
                self.error(f"Variable unassigned, can't read index at {statement.line}:{statement.column} scope({scope.name})")
            self.compile_indexed_variable_assignment(statement, var, scope)
            return
        func = self.compile_expression(statement.rhs, scope) # the value is on the stack now.
        if func is not None:
            self.scope.define_function_alias(statement.name, func.name)
        if  statement.op.type == AstNodetype.OPERATOR_ASSIGNMENT:
            if statement.append is True:
                reg = self.cs.GetFreeRegister()
                self.emit_pop(reg)                      # pop reg
                self.emit_load(self.cs.rax, var.stack_offset) # load rax, [rbp + stack_offset] rax is now the variable.
                self.cs.Emit_APPEND(self.cs.rax, reg)        # append rax, reg
                self.emit_stor(var.stack_offset, self.cs.rax) # stor [rbp + stack_offset], rax
                self.cs.ReleaseRegister(reg)
                return
            self.emit_pop(self.cs.rax)              # pop rax
            self.emit_stor(var.stack_offset, self.cs.rax) # stor [rbp + stack_offset], rax
            return
        # if it's not straight up assign, we need to do a binary operation with the variable value as the lhs, so we get it:
        self.emit_load(self.cs.rax, var.stack_offset) # load rax, [rbp + stack_offset] rax is now the variable.
        self.emit_pop(self.cs.rbx)              # pop rbx
        if statement.op.type == AstNodetype.OPERATOR_ASSIGNMENT_INC:
            self.cs.Emit_ADDRR(self.cs.rax, self.cs.rbx)        # addrr rax, rbx
        elif statement.op.type == AstNodetype.OPERATOR_ASSIGNMENT_DEC:
            self.cs.Emit_SUBRR(self.cs.rax, self.cs.rbx)        # subrr rax, rbx
        elif statement.op.type == AstNodetype.OPERATOR_ASSIGNMENT_MUL:
            self.cs.Emit_MULRR(self.cs.rax, self.cs.rbx)        # mulrr rax, rbx
        elif statement.op.type == AstNodetype.OPERATOR_ASSIGNMENT_DIV:
            self.cs.Emit_DIVRR(self.cs.rax, self.cs.rbx)        # divrr rax, rbx
        elif statement.op.type == AstNodetype.OPERATOR_ASSIGNMENT_MOD:
            self.cs.Emit_MODRR(self.cs.rax, self.cs.rbx)        # modrr rax, rbx
        elif statement.op.type == AstNodetype.OPERATOR_ASSIGNMENT_POW:
            self.cs.Emit_POWRR(self.cs.rax, self.cs.rbx)        # powrr rax, rbx
        self.emit_stor(var.stack_offset, self.cs.rax) # stor [rbp + stack_offset], rax

    # this is a continuation from compile_assign_statement where the variable is indexed.
    def compile_indexed_variable_assignment(self, statement: AstNodeAssignmentStatement, var: CTVariable, scope: CompilerScope) -> None:
        self.emit_new_label("assign_indexed", scope)
        if var.const:
            self.error(f"Cannot assign to const {statement.name} at {statement.line}:{statement.column} scope({scope.name})")
        self.var_to_stack(var)
        n = len(statement.lhs.index)
        if n > 1:
            for i in range(n-1):
                self.compile_expression(statement.lhs.index[i], scope)
                self.emit_pop(self.cs.rbx)              # pop rbx
                self.emit_pop(self.cs.rax)              # pop rax
                self.cs.Emit_INDEX()        # rax = rax[rbx]
                self.emit_push(self.cs.rax)             # push rax
        # at this point there should be something on the top of the stack that is
        # working as a reference, so if we assign to that it'll change the original with it.
        self.compile_expression(statement.lhs.index[n-1], scope)
        # on stack is now:
        # [0] = value
        # [1] = index
        # now we need to handle the right hand side of the assignment.
        self.compile_assign_indexed(statement.op, var, statement.rhs, scope)

    # this is a continuation from compile_indexed_variable_assignment, it handles the actual assignment.
    def compile_assign_indexed(self, op: LexToken, var: CTVariable, rhs: AstNodeExpression, scope: CompilerScope) -> None:
        if var.const:
            self.error(f"Cannot assign to const {var.name} at {rhs.line}:{rhs.column} scope({scope.name})")
        self.emit_new_label("assign_indexed_cnt", scope)
        func = self.compile_expression(rhs, scope) # the value is on the stack now.
        if func is not None:
            self.scope.define_function_alias(var.name, func.name)
        reg: BytecodeRegister = self.cs.GetFreeRegister()
        if  op.type == AstNodetype.OPERATOR_ASSIGNMENT:
            self.emit_pop(reg)                      # pop reg
            self.emit_pop(self.cs.rbx)              # pop rbx [index]
            self.emit_pop(self.cs.rax)              # pop rax [value]
            self.cs.Emit_INDEXR(reg)       # indexr rax[rbx] = reg
            self.cs.ReleaseRegister(reg)
            return
        self.emit_pop(reg)                      # pop reg => value to assign
        self.emit_pop(self.cs.rbx)              # pop rbx [index]
        self.emit_pop(self.cs.rax)              # pop rax [value]
        # rax[rbx] = LHS
        # reg      = RHS
        # We need to put rax and rbx back on the stack, because we need them later on.
        self.emit_push(self.cs.rax)              # push rax
        self.emit_push(self.cs.rbx)              # push rbx
        # Now get the value, so we can do something with it:
        self.cs.Emit_INDEX()  # pop rax = rax[rbx]
        self.emit_movrr(self.cs.rbx, reg) # movrr rbx = reg
        if op.type == AstNodetype.OPERATOR_ASSIGNMENT_INC:
            self.cs.Emit_ADDRR(self.cs.rax, self.cs.rbx)        # addrr rax, rbx
        elif op.type == AstNodetype.OPERATOR_ASSIGNMENT_DEC:
            self.cs.Emit_SUBRR(self.cs.rax, self.cs.rbx)        # subrr rax, rbx
        elif op.type == AstNodetype.OPERATOR_ASSIGNMENT_MUL:
            self.cs.Emit_MULRR(self.cs.rax, self.cs.rbx)        # mulrr rax, rbx
        elif op.type == AstNodetype.OPERATOR_ASSIGNMENT_DIV:
            self.cs.Emit_DIVRR(self.cs.rax, self.cs.rbx)        # divrr rax, rbx
        elif op.type == AstNodetype.OPERATOR_ASSIGNMENT_MOD:
            self.cs.Emit_MODRR(self.cs.rax, self.cs.rbx)        # modrr rax, rbx
        elif op.type == AstNodetype.OPERATOR_ASSIGNMENT_POW:
            self.cs.Emit_POWRR(self.cs.rax, self.cs.rbx)        # powrr rax, rbx
        self.emit_movrr(reg, self.cs.rax) # movrr reg = rax
        # reg is the resulting value, that we need to write as if it was a normal assign.
        self.emit_pop(self.cs.rbx)              # pop rbx [index]
        self.emit_pop(self.cs.rax)              # pop rax [value]
        self.cs.Emit_INDEXR(reg)       # indexr rax[rbx] = reg
        self.cs.ReleaseRegister(reg)
        self.emit_new_label("assign_indexed_cnt_end", scope)

    def has_params(self, params: List[AstNodeFunctionParameter]) -> bool:
        return any(param.type == AstNodetype.PARAMS for param in params)

    def compile_function_arguments(self, statement: AstNodeFunctionCallStatement, func: CTFunction, scope: CompilerScope) -> None:
        self.emit_new_label("function_arguments", scope)
        if len(statement.args) != len(func.parameters) and not self.has_params(func.parameters):
            self.error(f"Function {statement.name} at {statement.line}:{statement.column} scope({scope.name}) requires {len(func.parameters)} arguments, {len(statement.args)} given")
        for expr in statement.args:
            self.emit_new_label(f"function_argument: {expr}", scope)
            self.compile_expression(expr, scope)
        self.cs.Emit_MOVRI(self.cs.rax, AstNodetype.INTEGER, len(statement.args)) # function arguments count is in rax
        self.emit_push(self.cs.rax)              # push rax

    def compile_clean_function_arguments(self, statement: AstNodeFunctionCallStatement) -> None:
        # gets the return value from the stack, puts it in a temp reg, then pops all the arguments
        # from the stack and puts the return value back on the stack.
        # but only if the function had any arguments.
        reg = self.cs.GetFreeRegister()
        self.emit_pop(reg) # get the return value from the stack.
        if len(statement.args) > 0:
            for _ in range(len(statement.args)): # pop all the arguments from the stack.
                self.emit_pop(self.cs.rax)
        self.emit_pop(self.cs.rax) # pop the number of arguments value from the stack.
        self.emit_push(reg) #push the return value onto the stack again.
        self.cs.ReleaseRegister(reg)

    def compile_function_call(self, statement: AstNodeFunctionCallStatement, scope: CompilerScope) -> None:
        self.emit_new_label("function_call", scope)
        func = scope.get_function(statement.name)
        if func is None:
            var = scope.get_variable(statement.name)
            if var is not None:
                self.compile_variable_function_call(statement, var, scope)
                return
            self.error(f"Function {statement.name} not found at {statement.line}:{statement.column} scope({scope.name})")
        self.compile_function_arguments(statement, func, scope)
        self.emit_call(func.start_address)
        self.compile_clean_function_arguments(statement)
        self.emit_pop(self.cs.rax) # pop rax -> RAX has function return value.


    # this is a continuation of compile_function_call where the identifier is a variable instead of a function.
    def compile_variable_function_call(self, statement: AstNodeFunctionCallStatement, var: CTVariable, scope: CompilerScope) -> None:
        self.emit_new_label("variable_function_call", scope)
        # TODO: Make it so that it also works for indexed variable access.
        # It now only works based on the variable name, not on the index.
        # This bit is almost the same as it's the signature of the function call.
        #self.cs.write_string(var.name)
        func = scope.get_function_by_alias(var.name)
        if func is None:
            self.error(f"Function {statement.name} not found at {statement.line}:{statement.column} scope({scope.name})")
        self.compile_function_arguments(statement, func, scope)
        # So we are a variable, we need to figure out if we are a function pointer.
        self.emit_load(self.cs.rax, var.stack_offset) # load rax, [rbp + stack_offset] rax is now the variable.
        # rax is now the value of the variable.
        if statement.index is not None: # ok, we sneaked in an indexed one under the radar :P
            var.index = statement.index
            self.emit_push(self.cs.rax)              # push rax
            for i in range(len(var.index)):
                self.compile_expression(var.index[i], scope) # this pushes the result of the expression.
                self.emit_pop(self.cs.rbx)              # pop rbx
                self.emit_pop(self.cs.rax)              # pop rax
                self.cs.Emit_INDEX()        # rax = rax[rbx]
                self.emit_push(self.cs.rax)             # push rax
            self.emit_pop(self.cs.rax)              # pop rax
            self.cs.rax.type = AstNodetype.FUNCTION # this is needed, because inside the array this information was lost.
            self.cs.Emit_SETRTI(self.cs.rax, AstNodetype.FUNCTION)
        # validate if it is a function pointer.
        self.cs.Emit_CMPRTI(self.cs.rax, AstNodetype.FUNCTION) # compare register.type with immediate type
        self.cs.Emit_ERRORNZ(f"Variable {var.name} is not a function pointer. Scope({scope.name})") # error out when zero flag is not set.
        # if we get here, we have a valid function pointer in RAX
        # so we can call it.
        # warning cannot use rax in callr, callr destroys rax.
        self.cs.Emit_MOVRR(self.cs.rbx, self.cs.rax)
        self.emit_callr(self.cs.rbx)                # callr rbx
        self.compile_clean_function_arguments(statement)
        # The downside of this is that we can't change the location in memory for a function.
        # Unless we do some very elaborate work with setting the value of the variable to the correct address before
        # this is ran. But that is a problem for later.

    def compile_function_definition(self, statement: AstNodeFunctionDefinition, scope: CompilerScope) -> None:
        func = scope.define_function(statement.name, self.cs.rip.value+1) # +9 for the jump instruction.
        if func is None:
            self.error(f"Function {statement.name} already defined at {statement.line}:{statement.column} scope({scope.name})")
        function_label = scope.get_new_label(func.name)
        function_call_exit_label = self.get_new_label(f"{func.name}_exit", scope)
        function_call_end_label = self.get_new_label(f"{func.name}_end", scope)
        self.emit_jump(Opcode.JMP, function_call_end_label, scope) # functions go in between the other code, so we must jump over them.
        self.emit_label(function_label, scope)
        # make function scope.
        function_scope = self.emit_scope(scope)
        function_scope.is_function_definition = True
        function_scope.can_search_parent = False
        param_count = len(statement.parameters)
        for i, param in enumerate(statement.parameters):
            func.parameters.append(param)
            offset = FUNCTION_CALL_PARAMETER_STACK_OFFSET - (param_count-1) + i
            v = function_scope.define_variable(param.name, offset)
            v.type = param.type

        function_scope.exit_label = function_call_exit_label
        if statement.return_type is not None:
            func.return_type = statement.return_type
            function_scope.define_variable("return_value", FUNCTION_CALL_RETURN_VALUE_STACK_OFFSET)
        if statement.external:
            self.compile_external_function_definition(statement, func)
        else:
            self.compile_block(statement.body, function_scope)
        self.compile_function_definition_end(function_call_exit_label, function_call_end_label, function_scope)

    def compile_external_function_definition(self, statement: AstNodeFunctionDefinition, func: CTFunction) -> None:
        func.external = True
        func.module = statement.module
        func.function = statement.function
        self.cs.Emit_CALLE(func.module, func.function, len(statement.parameters))
        self.emit_storr(-3, self.cs.rax)  # storr [rbp - 3], rax

    def compile_function_definition_end(self, function_call_exit_label: int, function_call_end_label: int, scope: CompilerScope) -> None:
        self.emit_label(function_call_exit_label, scope)
        # exit label here.
        self.emit_scope_end(scope)
        self.cs.Emit_RET()          # ret
        # because rbp is popped after resetting the stack pointer,
        # the return value of the function is now on top of the stack.
        self.emit_label(function_call_end_label, scope)

    # Meta data compilation

    def compile_datasegment(self, scope: CompilerScope) -> None:
        metadata = {
            "VARIABLES": [var.name for var in scope.variables],
            "FUNCTIONS": [func.name for func in scope.functions],
            "LIBRARIES": [lib for lib in scope.libraries],
            "LABELS": [(label.name, label.address) for label in scope.labels],
            "JUMPS": [(jump.address, jump.label) for jump in scope.jump_table]
        }
        self.cs.Emit_DATASEG(metadata)

    # expression compilation

    def compile_expression(self, expression: AstNodeExpression, scope: CompilerScope) -> Optional[CTFunction]:
        self.emit_new_label("expression", scope) # up for commenting out, it's too chatty.
        if expression.type == AstNodetype.LITERAL_EXPRESSION:
            self.compile_literal_expression(expression, scope)
        elif expression.type == AstNodetype.UNARY_EXPRESSION:
            self.compile_unary_expression(expression, scope)
        elif expression.type == AstNodetype.BINARY_EXPRESSION:
            self.compile_binary_expression(expression, scope)
        elif expression.type == AstNodetype.VARIABLE_EXPRESSION:
            return self.compile_variable_expression(expression, scope)
        elif expression.type == AstNodetype.INDEXED_VARIABLE_EXPRESSION:
            self.compile_indexed_variable_expression(expression, scope)
        elif expression.type == AstNodetype.FUNCTION_CALL_EXPRESSION:
            return self.compile_function_call_expression(expression, scope)
        elif expression.type == AstNodetype.VARIABLE_FUNCTION_CALL_EXPRESSION:
            self.compile_variable_function_call_expression(expression, scope)
        elif expression.type == AstNodetype.IS_TYPE_STATEMENT:
            self.compile_is_type_statement(expression, scope)
        elif expression.type == AstNodetype.TYPE_STATEMENT:
            self.compile_type_statement(expression, scope)
        else:
            self.error(f"Unknown expression type {expression.type} at {expression.line}:{expression.column}")

    def compile_literal_expression(self, expression: AstNodeLiteralExpression, scope: CompilerScope) -> None:
        # A literal expression means a literal value gets written to the stack.
        self.emit_new_label("literal_expression", scope)
        if expression.value_type == AstNodetype.NEW_ARRAY:
            expression.value_type = AstNodetype.ARRAY
            expression.value = []
        self.cs.Emit_MOVRI(self.cs.rax, expression.value_type, expression.value)
        self.emit_push(self.cs.rax)

    def compile_unary_expression(self, expression: AstNodeUnaryExpression, scope: CompilerScope) -> None:
        self.emit_new_label("unary_expression", scope)
        self.compile_expression(expression.right, scope)
        self.emit_pop(self.cs.rax)              # pop rax
        if expression.op.type == AstNodetype.OPERATOR_SUBTRACTION:
            self.cs.Emit_NEG(self.cs.rax)
        elif expression.op.type == AstNodetype.NOT_STATEMENT:
            self.cs.Emit_NOT(self.cs.rax)
        elif expression.op.type == AstNodetype.BITWISE_NOT:
            self.error(f"Bitwise not not implemented at {expression.line}:{expression.column}")
        self.emit_push(self.cs.rax)

    def compile_binary_expression(self, expression: AstNodeBinaryExpression, scope: CompilerScope) -> None:
        self.emit_new_label("binary_expression", scope)
        # binary expression is simple. First we compile the left and right side of the expression
        # and then we pop the values in RAX and RBX apply the operator and then push RAX back onto the stack.
        self.compile_expression(expression.left, scope)
        self.compile_expression(expression.right, scope)
        self.emit_pop(self.cs.rbx)              # pop rbx rhs
        self.emit_pop(self.cs.rax)              # pop rax lhs
        if expression.op.type == AstNodetype.OPERATOR_ADDITION:
            self.cs.Emit_ADDRR(self.cs.rax, self.cs.rbx)   # addrr rax, rbx
        elif expression.op.type == AstNodetype.OPERATOR_SUBTRACTION:
            self.cs.Emit_SUBRR(self.cs.rax, self.cs.rbx)   # subrr rax, rbx
        elif expression.op.type == AstNodetype.OPERATOR_MULTIPLICATION:
            self.cs.Emit_MULRR(self.cs.rax, self.cs.rbx)   # mulrr rax, rbx
        elif expression.op.type == AstNodetype.OPERATOR_DIVISION:
            self.cs.Emit_DIVRR(self.cs.rax, self.cs.rbx)   # divrr rax, rbx
        elif expression.op.type == AstNodetype.OPERATOR_POWER:
            self.cs.Emit_POWRR(self.cs.rax, self.cs.rbx)   # powrr rax, rbx
        elif expression.op.type == AstNodetype.OPERATOR_MODULUS:
            self.cs.Emit_MODRR(self.cs.rax, self.cs.rbx)   # modrr rax, rbx
        elif expression.op.type  == AstNodetype.COMPARETOR_EQUAL:
            self.cs.Emit_CMPRR(self.cs.rax, self.cs.rbx)
            self.cs.Emit_SETZR(self.cs.rax)
        elif expression.op.type  == AstNodetype.COMPARETOR_NOT_EQUAL:
            self.cs.Emit_CMPRR(self.cs.rax, self.cs.rbx)
            self.cs.Emit_SETNZR(self.cs.rax)
        elif expression.op.type  == AstNodetype.COMPARETOR_LESS_THAN:
            self.cs.Emit_CMPRR(self.cs.rax, self.cs.rbx)
            self.cs.Emit_SETLR(self.cs.rax)
        elif expression.op.type  == AstNodetype.COMPARETOR_LESS_THAN_EQUAL:
            self.cs.Emit_CMPRR(self.cs.rax, self.cs.rbx)
            self.cs.Emit_SETLER(self.cs.rax)
        elif expression.op.type  == AstNodetype.COMPARETOR_GREATER_THAN:
            self.cs.Emit_CMPRR(self.cs.rax, self.cs.rbx)
            self.cs.Emit_SETGR(self.cs.rax)
        elif expression.op.type  == AstNodetype.COMPARETOR_GREATER_THAN_EQUAL:
            self.cs.Emit_CMPRR(self.cs.rax, self.cs.rbx)
            self.cs.Emit_SETGER(self.cs.rax)
        elif expression.op.type == AstNodetype.AND_STATEMENT:
            self.cs.Emit_ANDRR(self.cs.rax, self.cs.rbx)
        elif expression.op.type == AstNodetype.OR_STATEMENT:
            self.cs.Emit_ORRR(self.cs.rax, self.cs.rbx)
        elif expression.op.type == AstNodetype.XOR_STATEMENT:
            self.cs.Emit_XOR(self.cs.rax, self.cs.rbx)
        self.emit_push(self.cs.rax)              # push rax

    def compile_variable_expression(self, expression: AstNodeVariableExpression, scope: CompilerScope) -> Optional[CTFunction]:
        self.emit_new_label("variable_expression", scope)
        var = scope.get_variable(expression.name)
        if var is None:
            func = scope.get_function(expression.name)
            if func is not None:
                self.compile_function_expression(func)
                return func
            self.error(f"Variable or function {expression.name} not found at {expression.line}:{expression.column} scope({scope.name})")
        if not isinstance(var, CTVariable):
            self.error (f"Variable {expression.name} is not a variable at {expression.line}:{expression.column} scope({scope.name})")
        # variables live on the stack, the start of the stack for a scope is in the rbp register.
        # so we read the value from [rbp + var.offset] (our stack starts at 0 and counts up)
        # and push it to the stack.
        self.var_to_stack(var)

    def compile_indexed_variable_expression(self, expression: AstNodeIndexedVariableExpression, scope: CompilerScope) -> None:
        self.emit_new_label("indexed_variable_expression", scope)
        # Indexed variable expression is very hard.
        # Getting the variable is not a big deal, but handling the index is.
        var = scope.get_variable(expression.name)
        if var is None:
            self.error(f"Variable {expression.name} not defined at {expression.line}:{expression.column} scope({scope.name})")
        if not isinstance(var, CTVariable):
            self.error(f"Variable {expression.name} is not a variable at {expression.line}:{expression.column} scope({scope.name})")
        self.var_to_stack(var)
        # The variable value on the stack.
        # Now we need to get the index value.
        for expr in expression.index:
            self.compile_expression(expr, scope)    # the index value is on the stack now.
            self.emit_pop(self.cs.rbx)              # pop rbx
            self.emit_pop(self.cs.rax)              # pop rax
            self.cs.Emit_INDEX()        # rax = rax[rbx]
            self.emit_push(self.cs.rax)             # push rax

    def compile_function_expression(self, func: CTFunction) -> None:
        # This should only happen in an assignment.
        self.emit_new_label("function_expression", self.scope)
        self.cs.Emit_MOVRI(self.cs.rax, AstNodetype.FUNCTION, func.start_address)
        self.emit_push(self.cs.rax)

    def compile_function_call_expression(self, expression: AstNodeFunctionCallExpression, scope: CompilerScope) -> None:
        self.emit_new_label("function_call_expression", scope)
        func = scope.get_function(expression.name)
        if func is None: # maybe it's a variable? don't know, it should be handled by the other expr types.
            self.error(f"Function {expression.name} not found at {expression.line}:{expression.column} scope({scope.name})")
        self.compile_function_arguments(expression, func, scope)
        self.emit_call(func.start_address)
        self.compile_clean_function_arguments(expression)

    def compile_variable_function_call_expression(self, expression: AstNodeVariableFunctionCallExpression, scope: CompilerScope) -> None:
        self.emit_new_label("variable_function_call_expression", scope)
        var = scope.get_variable(expression.variable.name)
        if var is None:
            self.error(f"Variable {expression.variable.name} not defined at {expression.line}:{expression.column} scope({scope.name})")
        for expr in expression.args:
            self.compile_expression(expr)
        func = scope.get_function_by_alias(expression.variable.name)
        self.emit_call(func.start_address)
        self.compile_clean_function_arguments(expression)

    def compile_library_expression(self, expression: AstNodeLibraryExpression, scope: CompilerScope) -> None:
        self.error(f"Library expression not implemented at {expression.line}:{expression.column}")

# Include implementation

    def find_library(self, name: str) -> Optional[str]:
        for path in SearchPath:
            lib_path = os.path.join(path, f"{name}.mcl")
            if os.path.exists(lib_path):
                return lib_path
        return None

    def load_library(self, path: str) -> Optional[str]:
        if not os.path.exists(path):
            return None
        with open(path, "r") as f:
            return f.read()

    def compile_include_statement(self, statement: AstNodeIncludeStatement, scope: CompilerScope) -> None:
        self.emit_new_label("include_statement", scope)
        for lib in statement.libraries:
            if lib.name in scope.libraries:
                continue
            lib_path = self.find_library(lib.name)
            if lib_path is None:
                self.error(f"Library {lib.name} not found at {lib.line}:{lib.column}")
            source = self.load_library(lib_path)
            if source is None:
                self.error(f"Library {lib.name} not found at {lib.line}:{lib.column}")
            self.emit_new_label(f"include_{lib.name}", scope)
            self.scope.libraries[lib.name] = self.cs.rip.value
            lex = Lexer(source)
            parser = Parser(lex.tokenize(), lib_path)
            self.compile_block(parser.parse(), scope)

# end of file :)
