#!/usr/bin/env python3
"""
Nexo Programming Language - Parser (AST Builder)
محلل الجمل - بناء شجرة الجمل المجردة (AST)
"""

from dataclasses import dataclass
from typing import List, Optional, Any
from nexo_lexer import Token, TokenType, Lexer

# ===== عقد AST =====

@dataclass
class ASTNode:
    pass

@dataclass
class Program(ASTNode):
    statements: List[ASTNode]

@dataclass
class VariableDeclaration(ASTNode):
    name: str
    type_annotation: Optional[str]
    value: Optional[ASTNode]
    is_const: bool = False

@dataclass
class FunctionDeclaration(ASTNode):
    name: str
    parameters: List[tuple]  # [(name, type), ...]
    return_type: Optional[str]
    body: List[ASTNode]

@dataclass
class ClassDeclaration(ASTNode):
    name: str
    parent: Optional[str]
    interfaces: List[str]
    members: List[ASTNode]

@dataclass
class IfStatement(ASTNode):
    condition: ASTNode
    then_body: List[ASTNode]
    else_body: Optional[List[ASTNode]]

@dataclass
class ForLoop(ASTNode):
    variable: str
    iterable: ASTNode
    body: List[ASTNode]

@dataclass
class WhileLoop(ASTNode):
    condition: ASTNode
    body: List[ASTNode]

@dataclass
class ReturnStatement(ASTNode):
    value: Optional[ASTNode]

@dataclass
class FunctionCall(ASTNode):
    name: str
    arguments: List[ASTNode]

@dataclass
class BinaryOp(ASTNode):
    left: ASTNode
    operator: str
    right: ASTNode

@dataclass
class UnaryOp(ASTNode):
    operator: str
    operand: ASTNode

@dataclass
class Literal(ASTNode):
    value: Any
    type: str

@dataclass
class Identifier(ASTNode):
    name: str

@dataclass
class ListLiteral(ASTNode):
    elements: List[ASTNode]

@dataclass
class MapLiteral(ASTNode):
    pairs: List[tuple]  # [(key, value), ...]

@dataclass
class TryStatement(ASTNode):
    try_body: List[ASTNode]
    catch_clauses: List[tuple]  # [(exception_type, body), ...]
    finally_body: Optional[List[ASTNode]]

@dataclass
class ThrowStatement(ASTNode):
    exception: ASTNode

@dataclass
class ImportStatement(ASTNode):
    module: str
    items: Optional[List[str]]

# ===== Parser =====

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
    
    def current_token(self) -> Token:
        if self.pos >= len(self.tokens):
            return self.tokens[-1]  # EOF
        return self.tokens[self.pos]
    
    def peek_token(self, offset: int = 1) -> Token:
        pos = self.pos + offset
        if pos >= len(self.tokens):
            return self.tokens[-1]  # EOF
        return self.tokens[pos]
    
    def advance(self):
        self.pos += 1
    
    def expect(self, token_type: TokenType) -> Token:
        token = self.current_token()
        if token.type != token_type:
            raise SyntaxError(f"Expected {token_type}, got {token.type} at {token.line}:{token.column}")
        self.advance()
        return token
    
    def match(self, *token_types: TokenType) -> bool:
        return self.current_token().type in token_types
    
    def consume(self, token_type: TokenType) -> bool:
        if self.match(token_type):
            self.advance()
            return True
        return False
    
    def parse(self) -> Program:
        statements = []
        while not self.match(TokenType.EOF):
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        return Program(statements)
    
    def parse_statement(self) -> Optional[ASTNode]:
        if self.match(TokenType.LET, TokenType.VAR, TokenType.CONST):
            return self.parse_variable_declaration()
        elif self.match(TokenType.FUNC):
            return self.parse_function_declaration()
        elif self.match(TokenType.CLASS):
            return self.parse_class_declaration()
        elif self.match(TokenType.IF):
            return self.parse_if_statement()
        elif self.match(TokenType.FOR):
            return self.parse_for_loop()
        elif self.match(TokenType.WHILE):
            return self.parse_while_loop()
        elif self.match(TokenType.RETURN):
            return self.parse_return_statement()
        elif self.match(TokenType.TRY):
            return self.parse_try_statement()
        elif self.match(TokenType.THROW):
            return self.parse_throw_statement()
        elif self.match(TokenType.IMPORT):
            return self.parse_import_statement()
        elif self.match(TokenType.LBRACE):
            return self.parse_block()
        else:
            return self.parse_expression_statement()
    
    def parse_variable_declaration(self) -> VariableDeclaration:
        is_const = self.consume(TokenType.CONST)
        if not is_const:
            self.consume(TokenType.LET) or self.consume(TokenType.VAR)
        
        name_token = self.expect(TokenType.IDENTIFIER)
        name = name_token.value
        
        type_annotation = None
        if self.consume(TokenType.COLON):
            type_token = self.current_token()
            if type_token.type in (TokenType.INT, TokenType.FLOAT, TokenType.STRING, 
                                   TokenType.BOOL, TokenType.LIST, TokenType.MAP, 
                                   TokenType.TUPLE, TokenType.IDENTIFIER):
                type_annotation = type_token.value
                self.advance()
        
        value = None
        if self.consume(TokenType.ASSIGN):
            value = self.parse_expression()
        
        self.consume(TokenType.SEMICOLON)
        return VariableDeclaration(name, type_annotation, value, is_const)
    
    def parse_function_declaration(self) -> FunctionDeclaration:
        self.expect(TokenType.FUNC)
        name_token = self.expect(TokenType.IDENTIFIER)
        name = name_token.value
        
        self.expect(TokenType.LPAREN)
        parameters = self.parse_parameters()
        self.expect(TokenType.RPAREN)
        
        return_type = None
        if self.consume(TokenType.ARROW):
            return_type = self.current_token().value
            self.advance()
        
        self.expect(TokenType.LBRACE)
        body = self.parse_block_statements()
        self.expect(TokenType.RBRACE)
        
        return FunctionDeclaration(name, parameters, return_type, body)
    
    def parse_parameters(self) -> List[tuple]:
        parameters = []
        while not self.match(TokenType.RPAREN):
            name_token = self.expect(TokenType.IDENTIFIER)
            name = name_token.value
            
            param_type = None
            if self.consume(TokenType.COLON):
                param_type = self.current_token().value
                self.advance()
            
            parameters.append((name, param_type))
            
            if not self.consume(TokenType.COMMA):
                break
        
        return parameters
    
    def parse_class_declaration(self) -> ClassDeclaration:
        self.expect(TokenType.CLASS)
        name_token = self.expect(TokenType.IDENTIFIER)
        name = name_token.value
        
        parent = None
        if self.consume(TokenType.EXTENDS):
            parent = self.expect(TokenType.IDENTIFIER).value
        
        interfaces = []
        if self.consume(TokenType.IMPLEMENTS):
            interfaces.append(self.expect(TokenType.IDENTIFIER).value)
            while self.consume(TokenType.COMMA):
                interfaces.append(self.expect(TokenType.IDENTIFIER).value)
        
        self.expect(TokenType.LBRACE)
        members = self.parse_block_statements()
        self.expect(TokenType.RBRACE)
        
        return ClassDeclaration(name, parent, interfaces, members)
    
    def parse_if_statement(self) -> IfStatement:
        self.expect(TokenType.IF)
        condition = self.parse_expression()
        
        self.expect(TokenType.LBRACE)
        then_body = self.parse_block_statements()
        self.expect(TokenType.RBRACE)
        
        else_body = None
        if self.consume(TokenType.ELSE):
            if self.match(TokenType.IF):
                else_body = [self.parse_if_statement()]
            else:
                self.expect(TokenType.LBRACE)
                else_body = self.parse_block_statements()
                self.expect(TokenType.RBRACE)
        
        return IfStatement(condition, then_body, else_body)
    
    def parse_for_loop(self) -> ForLoop:
        self.expect(TokenType.FOR)
        variable = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.IDENTIFIER)  # 'in'
        iterable = self.parse_expression()
        
        self.expect(TokenType.LBRACE)
        body = self.parse_block_statements()
        self.expect(TokenType.RBRACE)
        
        return ForLoop(variable, iterable, body)
    
    def parse_while_loop(self) -> WhileLoop:
        self.expect(TokenType.WHILE)
        condition = self.parse_expression()
        
        self.expect(TokenType.LBRACE)
        body = self.parse_block_statements()
        self.expect(TokenType.RBRACE)
        
        return WhileLoop(condition, body)
    
    def parse_return_statement(self) -> ReturnStatement:
        self.expect(TokenType.RETURN)
        value = None
        if not self.match(TokenType.SEMICOLON, TokenType.RBRACE):
            value = self.parse_expression()
        self.consume(TokenType.SEMICOLON)
        return ReturnStatement(value)
    
    def parse_try_statement(self) -> TryStatement:
        self.expect(TokenType.TRY)
        self.expect(TokenType.LBRACE)
        try_body = self.parse_block_statements()
        self.expect(TokenType.RBRACE)
        
        catch_clauses = []
        while self.consume(TokenType.CATCH):
            self.expect(TokenType.LPAREN)
            exception_type = self.expect(TokenType.IDENTIFIER).value
            self.expect(TokenType.RPAREN)
            
            self.expect(TokenType.LBRACE)
            body = self.parse_block_statements()
            self.expect(TokenType.RBRACE)
            
            catch_clauses.append((exception_type, body))
        
        finally_body = None
        if self.consume(TokenType.IDENTIFIER):  # 'finally'
            self.expect(TokenType.LBRACE)
            finally_body = self.parse_block_statements()
            self.expect(TokenType.RBRACE)
        
        return TryStatement(try_body, catch_clauses, finally_body)
    
    def parse_throw_statement(self) -> ThrowStatement:
        self.expect(TokenType.THROW)
        exception = self.parse_expression()
        self.consume(TokenType.SEMICOLON)
        return ThrowStatement(exception)
    
    def parse_import_statement(self) -> ImportStatement:
        self.expect(TokenType.IMPORT)
        module = self.expect(TokenType.IDENTIFIER).value
        
        items = None
        if self.consume(TokenType.LBRACE):
            items = []
            items.append(self.expect(TokenType.IDENTIFIER).value)
            while self.consume(TokenType.COMMA):
                items.append(self.expect(TokenType.IDENTIFIER).value)
            self.expect(TokenType.RBRACE)
        
        self.consume(TokenType.SEMICOLON)
        return ImportStatement(module, items)
    
    def parse_block(self) -> List[ASTNode]:
        self.expect(TokenType.LBRACE)
        statements = self.parse_block_statements()
        self.expect(TokenType.RBRACE)
        return statements
    
    def parse_block_statements(self) -> List[ASTNode]:
        statements = []
        while not self.match(TokenType.RBRACE, TokenType.EOF):
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        return statements
    
    def parse_expression_statement(self) -> Optional[ASTNode]:
        expr = self.parse_expression()
        self.consume(TokenType.SEMICOLON)
        return expr
    
    def parse_expression(self) -> ASTNode:
        return self.parse_assignment()
    
    def parse_assignment(self) -> ASTNode:
        expr = self.parse_or()
        
        if self.match(TokenType.ASSIGN, TokenType.PLUS_ASSIGN, TokenType.MINUS_ASSIGN,
                      TokenType.STAR_ASSIGN, TokenType.SLASH_ASSIGN):
            op = self.current_token().value
            self.advance()
            right = self.parse_assignment()
            return BinaryOp(expr, op, right)
        
        return expr
    
    def parse_or(self) -> ASTNode:
        expr = self.parse_and()
        
        while self.match(TokenType.OR):
            op = self.current_token().value
            self.advance()
            right = self.parse_and()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def parse_and(self) -> ASTNode:
        expr = self.parse_equality()
        
        while self.match(TokenType.AND):
            op = self.current_token().value
            self.advance()
            right = self.parse_equality()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def parse_equality(self) -> ASTNode:
        expr = self.parse_comparison()
        
        while self.match(TokenType.EQ, TokenType.NE):
            op = self.current_token().value
            self.advance()
            right = self.parse_comparison()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def parse_comparison(self) -> ASTNode:
        expr = self.parse_range()
        
        while self.match(TokenType.LT, TokenType.LE, TokenType.GT, TokenType.GE):
            op = self.current_token().value
            self.advance()
            right = self.parse_range()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def parse_range(self) -> ASTNode:
        expr = self.parse_additive()
        
        if self.match(TokenType.RANGE):
            op = self.current_token().value
            self.advance()
            right = self.parse_additive()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def parse_additive(self) -> ASTNode:
        expr = self.parse_multiplicative()
        
        while self.match(TokenType.PLUS, TokenType.MINUS):
            op = self.current_token().value
            self.advance()
            right = self.parse_multiplicative()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def parse_multiplicative(self) -> ASTNode:
        expr = self.parse_power()
        
        while self.match(TokenType.STAR, TokenType.SLASH, TokenType.PERCENT):
            op = self.current_token().value
            self.advance()
            right = self.parse_power()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def parse_power(self) -> ASTNode:
        expr = self.parse_unary()
        
        if self.match(TokenType.POWER):
            op = self.current_token().value
            self.advance()
            right = self.parse_power()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def parse_unary(self) -> ASTNode:
        if self.match(TokenType.NOT, TokenType.MINUS, TokenType.PLUS):
            op = self.current_token().value
            self.advance()
            expr = self.parse_unary()
            return UnaryOp(op, expr)
        
        return self.parse_postfix()
    
    def parse_postfix(self) -> ASTNode:
        expr = self.parse_primary()
        
        while True:
            if self.consume(TokenType.LPAREN):
                arguments = self.parse_arguments()
                self.expect(TokenType.RPAREN)
                if isinstance(expr, Identifier):
                    expr = FunctionCall(expr.name, arguments)
            elif self.consume(TokenType.LBRACKET):
                index = self.parse_expression()
                self.expect(TokenType.RBRACKET)
                expr = BinaryOp(expr, '[]', index)
            elif self.consume(TokenType.DOT):
                member = self.expect(TokenType.IDENTIFIER).value
                expr = BinaryOp(expr, '.', Identifier(member))
            else:
                break
        
        return expr
    
    def parse_primary(self) -> ASTNode:
        if self.match(TokenType.NUMBER):
            value = self.current_token().value
            self.advance()
            return Literal(value, 'number')
        
        elif self.match(TokenType.STRING_LITERAL):
            value = self.current_token().value
            self.advance()
            return Literal(value, 'string')
        
        elif self.match(TokenType.TRUE, TokenType.FALSE):
            value = self.current_token().type == TokenType.TRUE
            self.advance()
            return Literal(value, 'bool')
        
        elif self.match(TokenType.NULL):
            self.advance()
            return Literal(None, 'null')
        
        elif self.match(TokenType.IDENTIFIER):
            name = self.current_token().value
            self.advance()
            return Identifier(name)
        
        elif self.consume(TokenType.LBRACKET):
            elements = []
            while not self.match(TokenType.RBRACKET):
                elements.append(self.parse_expression())
                if not self.consume(TokenType.COMMA):
                    break
            self.expect(TokenType.RBRACKET)
            return ListLiteral(elements)
        
        elif self.consume(TokenType.LBRACE):
            pairs = []
            while not self.match(TokenType.RBRACE):
                key = self.parse_expression()
                self.expect(TokenType.COLON)
                value = self.parse_expression()
                pairs.append((key, value))
                if not self.consume(TokenType.COMMA):
                    break
            self.expect(TokenType.RBRACE)
            return MapLiteral(pairs)
        
        elif self.consume(TokenType.LPAREN):
            expr = self.parse_expression()
            self.expect(TokenType.RPAREN)
            return expr
        
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token()}")
    
    def parse_arguments(self) -> List[ASTNode]:
        arguments = []
        while not self.match(TokenType.RPAREN):
            arguments.append(self.parse_expression())
            if not self.consume(TokenType.COMMA):
                break
        return arguments


def parse(source: str) -> Program:
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.parse()


if __name__ == "__main__":
    code = """
    let x: Int = 10
    let y: Int = 20
    
    func add(a: Int, b: Int) -> Int {
        return a + b
    }
    
    let result = add(x, y)
    print(result)
    """
    
    ast = parse(code)
    print(ast)
