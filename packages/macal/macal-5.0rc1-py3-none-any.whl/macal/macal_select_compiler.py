#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#


"""
    This module contains a separate compiler for the select statement.
    The select statement is very complex and requires a lot of code.
    Therefore i have decided to put that compiler code in a separate module.

    The Select Statement is a complex statement that can be used to select data from a table, a function call,
    a record or an array.

    The Select Statement is composed of the following parts:

    SELECT [DISTINCT] <field> [AS <altfield>], <field> [AS <altfield>], ...
    FROM <table>
    [WHERE <expression>]
    [MERGE]
    INTO <variable>

    The SELECT clause is a comma separated list of fields to select.
    The fields can only be identifiers.
    It is possible to use the AS keyword to rename the field in the result set.
    It is possible to use the * wildcard to select all fields.

    Fields are not required to exist. Non existing fields will be automatically added, with a NIL value.

    The optional DISTINCT keyword is different from the distinct keyword in SQL as so far
    that it will ensure that only a single record returns, it will only return the first record that matches the
    where clause.  If the where clause is not present, it will return the first record from the from clause.

    The FROM clause is the table to select from.
    It can be a variable, a function call or a literal.
    The content is required to be an array of records, or a single record.
    If only a single record is presented, then the record will be
    automatically put inside an array as the only element of that array.

    The optional WHERE clause is an expression that must evaluate to true for the record to be selected.

    The optional MERGE clause is used to merge the selected record into a variable.  If the variable is an array,
    the record is appended to the array.  If the variable is a record, the record is merged into the variable.
    Note that when merging into a record, any existing fields in the record will be overwritten by the
    fields in the selected record if there is any overlap.

    The INTO clause is the variable to store the selected record or records into.
    It can only be a variable.

    Examples:

    select * from my_variable into my_variable2;
    select * from my_function() into my_variable;
    select a as b, d as e from my_variable where a == 3 into my_variable2;

    The bytecode VM is a stack machine.  The stack machine has a stack and a program counter.

    The stack is a list of values.
    The program counter is an integer that points to the next instruction to execute.

    The stack machine has a set of instructions that can be executed.
    Each instruction has an opcode and one or more optional operands.

    The stack machine has a set of registers that can be used to store values.
    The registers are named as follows:
    RAX, RBX, RCX, RDX, RSI, RDI, RSP, RBP, R8, R9, R10, R11, R12, R13, R14, R15, RIP, FLAGS
    Contrary to normal CPU registers these registers have a value and a type field.
    The value field contains the value of the register.
    The type field contains the type of the value, the AstNodetype enum is used for this.
    The stack is a list of stack entries. The stack entries also have a value and a type field.
    The value can be any valid Python value.


The ARRAY is represented in Python as a list.
The RECORD is represented in Python as a dictionary.
Otherwise the value types are identical to the Python types.

"""
from __future__ import annotations
from .ast_nodetype import AstNodetype
from .ast_node_select_statement import AstNodeSelectStatement
from .ast_node_select_field import AstNodeSelectField
from .ast_node_expression import AstNodeExpression
from .ast_node_binary_expression import AstNodeBinaryExpression
from .ast_node_literal_expression import AstNodeLiteralExpression
from .ast_node_variable_expression import AstNodeVariableExpression
from .ast_node_unary_expression import AstNodeUnaryExpression
from .ast_node_indexed_variable_expression import AstNodeIndexedVariableExpression
from .macal_vm import MacalVm
from .macal_instructions import Opcode
from .bytecode_register import BytecodeRegister
from .compiler_scope import CompilerScope, CTVariable

# parent is the compiler, but we can't do that for reason of circular imports.
class MacalSelectCompiler:
    def __init__(self, parent) -> MacalSelectCompiler:
        self.do_raise: bool = parent.do_raise
        self.cs: MacalVm = parent.cs
        self.parent = parent

    def error(self, message: str) -> None:
        msg = f"SelectCompiler: {message}"
        if self.do_raise:
            raise Exception(msg)
        print(msg)
        import sys
        sys.exit(1)

    def compile_select(self, select: AstNodeSelectStatement, scope: CompilerScope) -> None:
        """
            This function compiles the given select statement into bytecode.
            The bytecode is returned as a list of tuples.
            Each tuple contains an opcode and a list of operands.
        """
        # Compile the from clause
        self.parent.emit_new_label("SELCT_FROM", scope)

        # SELECT FROM
        self.parent.compile_expression(select.From, scope)
        # Check if the result is a record or an array.

        lbl = self.parent.get_new_label("from_continue", scope)
        self.parent.emit_pop(self.cs.rax) # pop rax # rax has the value.
        self.cs.Emit_CMPRTI(self.cs.rax, AstNodetype.RECORD)
        self.parent.emit_jump(Opcode.JMPNZ, lbl, scope)
        # It's a record, for easy processing we move it into an array.
        self.cs.Emit_MOVRTOA(self.cs.rax) # rax = [rax]
        self.parent.emit_label(lbl, scope) # we jump here if it's an array or fall through to it if we have converted it to an array.
        self.parent.emit_push(self.cs.rax) # push rax # rax has the array.

        if select.Where is not None:
            # Compile the where clause
            self.parent.emit_new_label("SELECT_WHERE", scope)
            self.compile_where(select, scope)

        self.parent.emit_new_label("SELECT_FIELDS", scope)
        # Compile the select fields
        self.compile_select_fields(select, scope)

        # Compile the merge clause, only if its required.
        if select.merge is True:
            self.parent.emit_new_label("SELECT_MERGE", scope)
            self.compile_merge(select, scope)

        self.parent.emit_new_label("SELECT_INTO", scope)
        # Compile the into clause
        self.compile_into(select, scope)


    def compile_where(self, select: AstNodeSelectStatement, scope: CompilerScope) -> None:
        """
            This function compiles the where clause of the given select statement into bytecode.
            The bytecode is returned as a list of tuples.
            Each tuple contains an opcode and a list of operands.
        """
        # The core of this function is a loop that iterates over the array of records.
        # For each record it will evaluate the where clause.
        # If the where clause evaluates to true, the record will be added to the result array.
        # If the where clause evaluates to false, the record will be skipped.
        # The result array will be returned as the result of the where clause.
        # The result array will be a list of records, it will be empty if no records match the where clause.

        # Step 1: At the start of the where clause the array that was retrieved in the from clause is on the stack.
        # The rax register also has a copy of this.

        # We define labels for the start of the loop and the end of the loop.

        where_loop = self.parent.get_new_label("where_loop", scope)
        where_end  = self.parent.get_new_label("where_end", scope)

        # To know how much we need to loop for, we need to know the length of the array.
        # We will load the rcx register with the length. rcx is a special register that can be used in conjunction
        # with the djnz instruction.
        self.parent.emit_pop(self.cs.rax) # pop rax # rax has the array.
        self.cs.Emit_LENR(self.cs.rcx, self.cs.rax) # rcx = len(rax) and can be used for the DJNZ instruction.

        # To safeguard we need to check if the array actually has any elements.
        # If it doesn't we can skip the loop.
        self.cs.Emit_CMPRI(self.cs.rcx, AstNodetype.INTEGER, 0) # if rcx == 0, jump to where_end
        self.parent.emit_jump(Opcode.JMPZ, where_end, scope)

        # While RCX is used for iterating over the array, RBX is used for indexing into the array.
        # However RBX is a volatile register, so we acutally need another register to hold the index.
        index_register = self.cs.GetFreeRegister()
        self.cs.Emit_XOR(index_register, index_register) # rbx = 0 and can be used for indexing.

        source_register = self.cs.GetFreeRegister() # we get a free register to hold the source array in.
        self.cs.Emit_MOVRR(source_register, self.cs.rax) # source_register is now a "copy" of the array in rax.

        # We will request the VM for a free register to use for storing the resulting array of records
        result_register = self.cs.GetFreeRegister()
        self.cs.Emit_MOVRI(result_register, AstNodetype.ARRAY, []) # result_register is now an empty array.

        # We will also need to request the VM for a free register to temporarily store the current record.
        # This is so we can use the current record in the equasions of the where clause.
        record_register = self.cs.GetFreeRegister()

        skip_append = self.parent.get_new_label("skip_append", scope)

        self.parent.emit_label(where_loop, scope)  # this is where we return on each iteration of the loop.
        # At the start of the loop, we need the source array in the rax register and the index in the rbx register.
        self.cs.Emit_MOVRR(self.cs.rax, source_register) # rax is now the array
        self.cs.Emit_MOVRR(self.cs.rbx, index_register) # rbx is now the index
        self.cs.Emit_INDEX() # rax = rax[rbx] rax is now the current record.
        self.cs.Emit_MOVRR(record_register, self.cs.rax) # record_register is now a "copy" of the record in rax.

        self.compile_where_binary_expression(select.Where, record_register, scope) # we now execute the where clause.
        # Rax and rbx are destroyed in the process. The result will be on the stack. The result is either true or false.

        self.parent.emit_pop(self.cs.rax) # pop rax # rax has the result of the where clause.
        self.cs.Emit_CMPRI(self.cs.rax, AstNodetype.BOOLEAN, True) # if rax == True we need to include the record in the result array.
        # If rax is false, we need to skip to the next record.
        self.parent.emit_jump(Opcode.JMPNZ, skip_append, scope) # if rax == False, jump to skip_1

        self.cs.Emit_APPEND(result_register, record_register) # result_register[] = record_register
        # We now need to check if we need to continue to loop. If distinct is enabled, we can stop.
        self.cs.Emit_MOVRI(self.cs.rax, AstNodetype.BOOLEAN, select.distinct) # rax = select.distinct
        self.cs.Emit_CMPRI(self.cs.rax, AstNodetype.BOOLEAN, True) # if rax == True distinct is enabled and we can stop.
        self.parent.emit_jump(Opcode.JMPZ, where_end, scope) # if rax == True, jump to where_end
        self.parent.emit_label(skip_append, scope) # this is where we jump if we need to skip the record.
        self.cs.Emit_INC(index_register) # index = index + 1
        self.parent.emit_jump(Opcode.DJNZ, where_loop, scope) # rcx = rcx -1, if rcx != 0 jump to where_loop
        self.parent.emit_label(where_end, scope) # this is where we jump if we need to skip the loop.

        # We now need to push the result array onto the stack.
        self.parent.emit_push(result_register)
        # We can now release the registers that we used.
        self.cs.ReleaseRegister(source_register)
        self.cs.ReleaseRegister(index_register)
        self.cs.ReleaseRegister(result_register)
        self.cs.ReleaseRegister(record_register)


    def compile_select_fields(self, select: AstNodeSelectStatement, scope: CompilerScope) -> None:
        """
            This function compiles the code that will apply the field selection to the result of the from clause.
            (or the where clause if that exists)
        """
        self.parent.emit_new_label("fields", scope)
        # Compile the select fields
        if len(select.Fields) == 1 and select.Fields[0].fieldname == '*':
            return # no need to do anything with the fields.
        # The fields are basically a filter on the result of the from clause or the where clause.
        # The result of the from clause or the where clause is on the stack.

        self.parent.emit_pop(self.cs.rax) # pop rax rax is now the array.
        # We will request the VM for a free register to use for temporary storing array of records
        array_register = self.cs.GetFreeRegister()
        self.cs.Emit_MOVRR(array_register, self.cs.rax) # array_register is now a "copy" of the array in rax.

        # We need another register to store the result of the field selection in the array.
        result_array_register = self.cs.GetFreeRegister()
        self.cs.Emit_MOVRI(result_array_register, AstNodetype.ARRAY, [])

        # we need yet another register to store the result for the field selection in the individual records.
        result_record_register = self.cs.GetFreeRegister()
        # We need another register to store the current record.
        current_record_register = self.cs.GetFreeRegister()
        # And another register to store the index register.
        index_register = self.cs.GetFreeRegister()
        # and another register to store the field value.
        field_value_register = self.cs.GetFreeRegister()

        # setup the index.
        self.cs.Emit_XOR(self.cs.rbx, self.cs.rbx) # rbx = 0
        self.cs.Emit_MOVRR(index_register, self.cs.rbx) # index_register = rbx (rbx is 0

        # setup the loop.
        array_loop_label = self.parent.get_new_label("allbl", scope)
        array_continue_label = self.parent.get_new_label("aclbl", scope)

        self.cs.Emit_LENR(self.cs.rcx, self.cs.rax) # rcx = len(rax) and can be used for the DJNZ instruction.

        self.parent.emit_label(array_loop_label, scope)
        # the array loop starts here.
        # First we get RAX and RBX set up with the array and index.
        self.cs.Emit_MOVRR(self.cs.rax, array_register) # rax is now the array again.
        self.cs.Emit_MOVRR(self.cs.rbx, index_register) # rbx is now the index again.

        # We get the current record:
        self.cs.Emit_INDEX() # rax = rax[rbx]
        # We check if it is a record:
        self.cs.Emit_CMPRTI(self.cs.rax, AstNodetype.RECORD)
        self.cs.Emit_ERRORNZ("Expected a record in the FROM clause of the SELECT statement.")
        # rax is now assured to be a record.
        self.cs.Emit_MOVRR(current_record_register, self.cs.rax) # current_record_register is now a "copy" of the record in rax.
        # for each record that we process we need a new result record:
        self.cs.Emit_MOVRI(result_record_register, AstNodetype.RECORD, {})

        for field in select.Fields: # we unroll this loop to prevent nested loops.
            self.compile_field(field, current_record_register, result_record_register, field_value_register, scope)
        # Append the result record to the result array.
        self.cs.Emit_MOVRR(self.cs.rax, result_array_register) # rax is now the result array.
        self.cs.Emit_APPEND(self.cs.rax, result_record_register) # rax[] = result_record_register

        # store the result array back into result_array_register.
        self.cs.Emit_MOVRR(result_array_register, self.cs.rax) # result_array_register = rax

        # we're done with this record, so we increment the index.
        self.cs.Emit_INC(index_register) # rbx = rbx + 1
        # and we check if we're done.
        # Only continue to loop if Distinct is False.
        # With Distinct True we only need the first matching record.
        if select.distinct is False:
            self.parent.emit_jump(Opcode.DJNZ, array_loop_label, scope) # rcx = rcx -1, if rcx != 0 jump to array_loop_label

        # if it falls through we're done.
        self.parent.emit_label(array_continue_label, scope)
        self.parent.emit_push(result_array_register) # result is now on the stack.
        self.cs.ReleaseRegister(array_register)
        self.cs.ReleaseRegister(result_array_register)
        self.cs.ReleaseRegister(result_record_register)
        self.cs.ReleaseRegister(current_record_register)
        self.cs.ReleaseRegister(index_register)
        self.cs.ReleaseRegister(field_value_register)

    def compile_field(self, field: AstNodeSelectField, record_register: BytecodeRegister,
                      result_record_register: BytecodeRegister, field_value_register: BytecodeRegister, scope: CompilerScope) -> None:
        new_record_field = self.cs.GetFreeRegister()
        self.cs.Emit_MOVRI(new_record_field, AstNodetype.NIL, AstNodetype.NIL)
        has_fld_lbl = self.parent.get_new_label("has_fld", scope)
        self.cs.Emit_MOVRR(self.cs.rax, record_register) # rax is the current record
        self.cs.Emit_MOVRI(self.cs.rbx, AstNodetype.STRING, field.fieldname) # rbx is the original name of the field
        self.cs.Emit_HASFLDRR(self.cs.rax, self.cs.rbx)

        self.parent.emit_jump(Opcode.JMPZ, has_fld_lbl, scope)
        # The field does not exist in the record, so we need to create it.
        self.cs.Emit_INDEXR(new_record_field)
        self.cs.Emit_MOVRR(record_register, self.cs.rax)
        self.parent.emit_label(has_fld_lbl, scope)
        self.cs.Emit_INDEX() # rax = rax[rbx] rax is now the value of the field.
        self.cs.Emit_MOVRI(self.cs.rbx, AstNodetype.STRING, field.altfieldname) # rbx is now the new field name.
        self.cs.Emit_MOVRR(field_value_register, self.cs.rax) # field_value_register is now a "copy" of the field value in rax.
        self.cs.Emit_MOVRR(self.cs.rax, result_record_register) # rax is now the result record.
        self.cs.Emit_INDEXR(field_value_register) # # rax[rbx] = field_value_register so we add the current new field to the resulting record.
        self.cs.Emit_MOVRR(result_record_register, self.cs.rax) # result_record_register is now a "copy" of the result record in rax.
        self.cs.ReleaseRegister(new_record_field)

    def compile_into(self, select: AstNodeSelectStatement, scope: CompilerScope) -> None:
        # Get the into variable if it exists, or create a new one, put the result on the stack.
        into: CTVariable = scope.find_variable(select.Into.value)
        self.parent.emit_pop(self.cs.rax) # pop rax # rax has the value.
        if into is None:
            self.parent.emit_new_label("into need a new var", scope)
            # it doesn't exist so we make one.
            reg = self.cs.GetFreeRegister()
            self.cs.Emit_XOR(reg, reg)
            into = scope.define_variable(select.Into.value, self.cs.rsp.value)
            self.cs.Emit_MOVRR(self.cs.rbx,self.cs.rsp) # rbx is now the absolute index of the new variable in the stack.
            self.parent.emit_push(reg)
            self.cs.ReleaseRegister(reg)
        else:
            self.cs.Emit_MOVRI(self.cs.rbx, AstNodetype.INTEGER, into.stack_offset)

        self.cs.Emit_STORIR(self.cs.rbx, self.cs.rax) # [rbx] = rax
        # we have now stored the result into the variable.

    def compile_merge(self, select: AstNodeSelectStatement, scope: CompilerScope) -> None:
        into: CTVariable = scope.find_variable(select.Into.value)
        if into is None:
            self.error(f"Variable not found ({select.Into.value}) at line: {select.Into.lineno}, column: {select.Into.offset}.")
        source_reg = self.cs.GetFreeRegister()
        data_reg = self.cs.GetFreeRegister()
        dest_reg = self.cs.GetFreeRegister()
        self.cs.Emit_LOAD(source_reg, into.stack_offset)        # load the variable into source_reg.
        self.parent.emit_pop(data_reg)                          # pop data_reg with the data to merge.
        self.cs.Emit_MOVRI(dest_reg, AstNodetype.ARRAY, [])     # setup the destination array.
        self.cs.Emit_MERGE(dest_reg, source_reg, data_reg)      # merge the source and data into dest.
        self.parent.emit_push(dest_reg)                         # push the result onto the stack.
        self.cs.ReleaseRegister(source_reg)
        self.cs.ReleaseRegister(data_reg)
        self.cs.ReleaseRegister(dest_reg)

# Where specific expression compilation.

    def compile_where_expression(self, expr: AstNodeExpression, record_register: BytecodeRegister, scope: CompilerScope):
        if expr.type == AstNodetype.BINARY_EXPRESSION:
            self.compile_where_binary_expression(expr, record_register, scope)
        elif expr.type == AstNodetype.LITERAL_EXPRESSION:
            self.compile_where_literal_expression(expr, scope)
        elif expr.type == AstNodetype.FUNCTION_CALL_EXPRESSION:
            self.parent.compile_function_call_expression(expr, scope)
        elif expr.type == AstNodetype.VARIABLE_EXPRESSION:
            self.compile_where_variable_expression(expr, record_register, scope)
        elif expr.type == AstNodetype.UNARY_EXPRESSION:
            self.compile_where_unary_expression(expr, record_register, scope)
        elif expr.type == AstNodetype.INDEXED_VARIABLE_EXPRESSION:
            self.compile_where_indexed_variable_expression(expr, record_register, scope)
        else:
            self.error(f"Unexpected expression type {expr.type.name} in WHERE clause.")

    def compile_where_binary_expression(self, where: AstNodeBinaryExpression,
                                        record_register: BytecodeRegister, scope: CompilerScope) -> None:
        # The were clause consists of binary expressions that will evaluate to a boolean value true or false.

        # The record to evaluate is in the rax register, a copy of that record is in the record_register.
        # The result of the where clause will be stored in the rax register.

        # The where clause is a binary expression, so we need to evaluate the left and right side of the expression.
        # The result of the left side of the expression will be stored in the rax register.
        # The result of the right side of the expression will be stored in the rbx register.
        # The result of the where clause will be stored in the rax register.

        # The left side of the expression is a fieldname in the record.
        # The operator is a comparison operator
        # The right side is a literal, a variable, a function call resulting in a literal, or another binary expression.
        # There may be multiple levels deep if the right hand side is a binary expression.
        # (This happens if and/or/not/xor is used in the where clause.)
        self.compile_where_expression(where.left, record_register, scope)
        # LHS is now on the stack.
        self.compile_where_expression(where.right, record_register, scope)
        # RHS is now on the stack.
        # We now need to compare the LHS and RHS using our operator.
        # The result of the comparison will be stored in the rax register.
        self.parent.emit_pop(self.cs.rbx)
        self.parent.emit_pop(self.cs.rax)
        self.cs.Emit_CMPRR(self.cs.rax, self.cs.rbx)
        # The result of the comparison is now in the FLAGS register.
        # Based on the flags and our operator we can set the rax register to True or False.
        if where.op.value == '==':
            self.cs.Emit_SETZR(self.cs.rax)
        elif where.op.value == '!=':
            self.cs.Emit_SETNZR(self.cs.rax)
        elif where.op.value == '<':
            self.cs.Emit_SETLR(self.cs.rax)
        elif where.op.value == '<=':
            self.cs.Emit_SETLER(self.cs.rax)
        elif where.op.value == '>':
            self.cs.Emit_SETGR(self.cs.rax)
        elif where.op.value == '>=':
            self.cs.Emit_SETGER(self.cs.rax)
        else:
            self.error(f"Illegal operator {where.op.value} in WHERE clause.")
        self.parent.emit_push(self.cs.rax) # push result on register!

    def compile_where_literal_expression(self,
                                         expression: AstNodeLiteralExpression,
                                         scope: CompilerScope) -> None:
        # A literal expression means a literal value gets written to the stack.
        self.cs.Emit_MOVRI(self.cs.rax, expression.value_type, expression.value)
        self.parent.emit_push(self.cs.rax)

    def compile_where_unary_expression(self
                                       , expression: AstNodeUnaryExpression
                                       , record_register: BytecodeRegister
                                       , scope: CompilerScope) -> None:
        lbl = scope.get_new_label("unary_expression", scope)
        self.parent.emit_label(lbl, scope)
        self.compile_where_expression(expression.right, record_register, scope)
        self.parent.emit_pop(self.cs.rax) # pop rax
        if expression.op.type == AstNodetype.OPERATOR_SUBTRACTION:
            self.cs.Emit_NEG(self.cs.rax)
        elif expression.op.type == AstNodetype.NOT_STATEMENT:
            self.cs.Emit_NOT(self.cs.rax)
        elif expression.op.type == AstNodetype.BITWISE_NOT:
            self.error("Bitwise not is not yet implemented.")
        self.parent.emit_push(self.cs.rax)

    def compile_where_variable_expression(self
                                          , expression: AstNodeVariableExpression
                                          , record_register: BytecodeRegister
                                          , scope: CompilerScope) -> None:
        lbl = scope.get_new_label("variable_where_expression")
        self.parent.emit_label(lbl, scope)
        var = scope.find_variable(expression.name)
        if var is None:
            # The variable should be a field in the record.
            # We need to push the value of the field onto the stack.
            self._record_field_to_stack(expression.name, record_register)
            return
        if not isinstance(var, CTVariable):
            self.error (f"Variable {expression.name} is not a variable at {expression.line}:{expression.column} scope({scope.name})")
        # variables live on the stack, the start of the stack for a scope is in the rbp register.
        # so we read the value from [rbp + var.offset] (our stack starts at 0 and counts up)
        # and push it to the stack.
        self.parent.var_to_stack(var, scope)

    def compile_where_indexed_variable_expression(self
                                                  , expression: AstNodeIndexedVariableExpression
                                                  , record_register: BytecodeRegister
                                                  , scope: CompilerScope) -> None:
        lbl = scope.get_new_label("indexed_variable_expression")
        self.parent.emit_label(lbl, scope)
        var = scope.get_variable(expression.name)
        if var is None:
            # The variable is a field in the record.
            self._record_field_to_stack(expression.name, record_register, scope)
        else:
            # if it's just a var, get it.
            if not isinstance(var, CTVariable):
                self.error(f"Variable {expression.name} is not a variable at {expression.line}:{expression.column} scope({scope.name})")
            self.parent.var_to_stack(var, scope) # store the var on the stack.
        self.walk_index(expression, scope)

######################### Shared Helper Functions #########################################

    def _record_field_to_stack(self, name: str, record_register: BytecodeRegister) -> None:
        # rax record , rax = rax[rbx], push rax
        self.cs.Emit_MOVRR(self.cs.rax, record_register) # rax = record
        self.cs.Emit_MOVRI(self.cs.rbx, AstNodetype.STRING, name) # rbx = name
        self.cs.Emit_INDEX() # rax = rax[rbx]
        self.parent.emit_push(self.cs.rax)


    def walk_index(self, expression: AstNodeExpression, scope: CompilerScope) -> None:
        for expr in expression.index:                     # we walk each index part.
            self.compile_where_expression(expr, scope)    # the index value is on the stack now.
            self.parent.emit_pop(self.cs.rbx)             # pop rbx
            self.parent.emit_pop(self.cs.rax)             # pop rax
            self.cs.Emit_INDEX()                          # rax = rax[rbx]
            self.parent.emit_push(self.cs.rax)            # push rax

###########################################################################################################
