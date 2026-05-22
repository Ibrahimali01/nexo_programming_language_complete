#!/usr/bin/env python3
"""
Nexo Programming Language - Lexer (Tokenizer)
المحلل اللغوي - تحويل النصوص إلى رموز (Tokens)
"""

import re
from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Optional

class TokenType(Enum):
    # الكلمات المفتاحية
    LET = auto()
    VAR = auto()
    CONST = auto()
    FUNC = auto()
    CLASS = auto()
    INTERFACE = auto()
    EXTENDS = auto()
    IMPLEMENTS = auto()
    RETURN = auto()
    IF = auto()
    ELSE = auto()
    FOR = auto()
    WHILE = auto()
    SWITCH = auto()
    CASE = auto()
    DEFAULT = auto()
    BREAK = auto()
    CONTINUE = auto()
    TRY = auto()
    CATCH = auto()
    THROW = auto()
    IMPORT = auto()
    EXPORT = auto()
    ASYNC = auto()
    AWAIT = auto()
    STATIC = auto()
    CONSTRUCTOR = auto()
    THIS = auto()
    SUPER = auto()
    NEW = auto()
    TRUE = auto()
    FALSE = auto()
    NULL = auto()
    VOID = auto()
    THROWS = auto()
    
    # الأنواع
    INT = auto()
    FLOAT = auto()
    STRING = auto()
    BOOL = auto()
    LIST = auto()
    MAP = auto()
    TUPLE = auto()
    
    # المعاملات
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    PERCENT = auto()
    POWER = auto()
    ASSIGN = auto()
    PLUS_ASSIGN = auto()
    MINUS_ASSIGN = auto()
    STAR_ASSIGN = auto()
    SLASH_ASSIGN = auto()
    
    # المقارنات
    EQ = auto()
    NE = auto()
    LT = auto()
    LE = auto()
    GT = auto()
    GE = auto()
    AND = auto()
    OR = auto()
    NOT = auto()
    
    # الفواصل
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    SEMICOLON = auto()
    COMMA = auto()
    DOT = auto()
    COLON = auto()
    ARROW = auto()
    DOUBLE_COLON = auto()
    RANGE = auto()
    ELLIPSIS = auto()
    
    # الحرفيات
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING_LITERAL = auto()
    
    # خاص
    EOF = auto()
    NEWLINE = auto()
    ERROR = auto()

@dataclass
class Token:
    type: TokenType
    value: any
    line: int
    column: int
    
    def __repr__(self):
        return f"Token({self.type.name}, {self.value!r}, {self.line}:{self.column})"

class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
        
        # الكلمات المفتاحية
        self.keywords = {
            'let': TokenType.LET,
            'var': TokenType.VAR,
            'const': TokenType.CONST,
            'func': TokenType.FUNC,
            'class': TokenType.CLASS,
            'interface': TokenType.INTERFACE,
            'extends': TokenType.EXTENDS,
            'implements': TokenType.IMPLEMENTS,
            'return': TokenType.RETURN,
            'if': TokenType.IF,
            'else': TokenType.ELSE,
            'for': TokenType.FOR,
            'while': TokenType.WHILE,
            'switch': TokenType.SWITCH,
            'case': TokenType.CASE,
            'default': TokenType.DEFAULT,
            'break': TokenType.BREAK,
            'continue': TokenType.CONTINUE,
            'try': TokenType.TRY,
            'catch': TokenType.CATCH,
            'throw': TokenType.THROW,
            'import': TokenType.IMPORT,
            'export': TokenType.EXPORT,
            'async': TokenType.ASYNC,
            'await': TokenType.AWAIT,
            'static': TokenType.STATIC,
            'constructor': TokenType.CONSTRUCTOR,
            'this': TokenType.THIS,
            'super': TokenType.SUPER,
            'new': TokenType.NEW,
            'true': TokenType.TRUE,
            'false': TokenType.FALSE,
            'null': TokenType.NULL,
            'void': TokenType.VOID,
            'throws': TokenType.THROWS,
            'Int': TokenType.INT,
            'Float': TokenType.FLOAT,
            'String': TokenType.STRING,
            'Bool': TokenType.BOOL,
            'List': TokenType.LIST,
            'Map': TokenType.MAP,
            'Tuple': TokenType.TUPLE,
        }
    
    def current_char(self) -> Optional[str]:
        if self.pos >= len(self.source):
            return None
        return self.source[self.pos]
    
    def peek_char(self, offset: int = 1) -> Optional[str]:
        pos = self.pos + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]
    
    def advance(self):
        if self.pos < len(self.source):
            if self.source[self.pos] == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.pos += 1
    
    def skip_whitespace(self):
        while self.current_char() and self.current_char() in ' \t\r':
            self.advance()
    
    def skip_comment(self):
        if self.current_char() == '/' and self.peek_char() == '/':
            while self.current_char() and self.current_char() != '\n':
                self.advance()
        elif self.current_char() == '/' and self.peek_char() == '*':
            self.advance()
            self.advance()
            while self.current_char():
                if self.current_char() == '*' and self.peek_char() == '/':
                    self.advance()
                    self.advance()
                    break
                self.advance()
    
    def read_string(self, quote: str) -> str:
        result = ""
        self.advance()  # تخطي علامة الاقتباس
        
        while self.current_char() and self.current_char() != quote:
            if self.current_char() == '\\':
                self.advance()
                if self.current_char() == 'n':
                    result += '\n'
                elif self.current_char() == 't':
                    result += '\t'
                elif self.current_char() == 'r':
                    result += '\r'
                elif self.current_char() == '\\':
                    result += '\\'
                elif self.current_char() == quote:
                    result += quote
                self.advance()
            else:
                result += self.current_char()
                self.advance()
        
        if self.current_char() == quote:
            self.advance()
        
        return result
    
    def read_number(self) -> Token:
        start_line = self.line
        start_column = self.column
        num_str = ""
        
        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            num_str += self.current_char()
            self.advance()
        
        if '.' in num_str:
            return Token(TokenType.NUMBER, float(num_str), start_line, start_column)
        else:
            return Token(TokenType.NUMBER, int(num_str), start_line, start_column)
    
    def read_identifier(self) -> Token:
        start_line = self.line
        start_column = self.column
        ident = ""
        
        while self.current_char() and (self.current_char().isalnum() or self.current_char() in '_'):
            ident += self.current_char()
            self.advance()
        
        token_type = self.keywords.get(ident, TokenType.IDENTIFIER)
        
        if token_type in (TokenType.TRUE, TokenType.FALSE):
            return Token(token_type, ident == 'true', start_line, start_column)
        elif token_type == TokenType.NULL:
            return Token(token_type, None, start_line, start_column)
        else:
            return Token(token_type, ident, start_line, start_column)
    
    def tokenize(self) -> List[Token]:
        while self.pos < len(self.source):
            self.skip_whitespace()
            
            if self.current_char() == '\n':
                self.advance()
                continue
            
            if self.current_char() == '/' and (self.peek_char() == '/' or self.peek_char() == '*'):
                self.skip_comment()
                continue
            
            char = self.current_char()
            line = self.line
            column = self.column
            
            if char is None:
                break
            
            # الأرقام
            if char.isdigit():
                self.tokens.append(self.read_number())
            
            # المعرّفات والكلمات المفتاحية
            elif char.isalpha() or char == '_':
                self.tokens.append(self.read_identifier())
            
            # النصوص
            elif char in ('"', "'"):
                string_value = self.read_string(char)
                self.tokens.append(Token(TokenType.STRING_LITERAL, string_value, line, column))
            
            # المعاملات والفواصل
            elif char == '+':
                self.advance()
                if self.current_char() == '=':
                    self.advance()
                    self.tokens.append(Token(TokenType.PLUS_ASSIGN, '+=', line, column))
                else:
                    self.tokens.append(Token(TokenType.PLUS, '+', line, column))
            
            elif char == '-':
                self.advance()
                if self.current_char() == '=':
                    self.advance()
                    self.tokens.append(Token(TokenType.MINUS_ASSIGN, '-=', line, column))
                elif self.current_char() == '>':
                    self.advance()
                    self.tokens.append(Token(TokenType.ARROW, '->', line, column))
                else:
                    self.tokens.append(Token(TokenType.MINUS, '-', line, column))
            
            elif char == '*':
                self.advance()
                if self.current_char() == '=':
                    self.advance()
                    self.tokens.append(Token(TokenType.STAR_ASSIGN, '*=', line, column))
                elif self.current_char() == '*':
                    self.advance()
                    self.tokens.append(Token(TokenType.POWER, '**', line, column))
                else:
                    self.tokens.append(Token(TokenType.STAR, '*', line, column))
            
            elif char == '/':
                self.advance()
                if self.current_char() == '=':
                    self.advance()
                    self.tokens.append(Token(TokenType.SLASH_ASSIGN, '/=', line, column))
                else:
                    self.tokens.append(Token(TokenType.SLASH, '/', line, column))
            
            elif char == '%':
                self.advance()
                self.tokens.append(Token(TokenType.PERCENT, '%', line, column))
            
            elif char == '=':
                self.advance()
                if self.current_char() == '=':
                    self.advance()
                    self.tokens.append(Token(TokenType.EQ, '==', line, column))
                else:
                    self.tokens.append(Token(TokenType.ASSIGN, '=', line, column))
            
            elif char == '!':
                self.advance()
                if self.current_char() == '=':
                    self.advance()
                    self.tokens.append(Token(TokenType.NE, '!=', line, column))
                else:
                    self.tokens.append(Token(TokenType.NOT, '!', line, column))
            
            elif char == '<':
                self.advance()
                if self.current_char() == '=':
                    self.advance()
                    self.tokens.append(Token(TokenType.LE, '<=', line, column))
                elif self.current_char() == '<':
                    self.advance()
                    self.tokens.append(Token(TokenType.DOUBLE_COLON, '<<', line, column))
                else:
                    self.tokens.append(Token(TokenType.LT, '<', line, column))
            
            elif char == '>':
                self.advance()
                if self.current_char() == '=':
                    self.advance()
                    self.tokens.append(Token(TokenType.GE, '>=', line, column))
                elif self.current_char() == '>':
                    self.advance()
                    self.tokens.append(Token(TokenType.DOUBLE_COLON, '>>', line, column))
                else:
                    self.tokens.append(Token(TokenType.GT, '>', line, column))
            
            elif char == '&':
                self.advance()
                if self.current_char() == '&':
                    self.advance()
                    self.tokens.append(Token(TokenType.AND, '&&', line, column))
            
            elif char == '|':
                self.advance()
                if self.current_char() == '|':
                    self.advance()
                    self.tokens.append(Token(TokenType.OR, '||', line, column))
            
            elif char == '(':
                self.advance()
                self.tokens.append(Token(TokenType.LPAREN, '(', line, column))
            
            elif char == ')':
                self.advance()
                self.tokens.append(Token(TokenType.RPAREN, ')', line, column))
            
            elif char == '{':
                self.advance()
                self.tokens.append(Token(TokenType.LBRACE, '{', line, column))
            
            elif char == '}':
                self.advance()
                self.tokens.append(Token(TokenType.RBRACE, '}', line, column))
            
            elif char == '[':
                self.advance()
                self.tokens.append(Token(TokenType.LBRACKET, '[', line, column))
            
            elif char == ']':
                self.advance()
                self.tokens.append(Token(TokenType.RBRACKET, ']', line, column))
            
            elif char == ';':
                self.advance()
                self.tokens.append(Token(TokenType.SEMICOLON, ';', line, column))
            
            elif char == ',':
                self.advance()
                self.tokens.append(Token(TokenType.COMMA, ',', line, column))
            
            elif char == '.':
                self.advance()
                if self.current_char() == '.' and self.peek_char() == '.':
                    self.advance()
                    self.advance()
                    self.tokens.append(Token(TokenType.ELLIPSIS, '...', line, column))
                elif self.current_char() == '.':
                    self.advance()
                    self.tokens.append(Token(TokenType.RANGE, '..', line, column))
                else:
                    self.tokens.append(Token(TokenType.DOT, '.', line, column))
            
            elif char == ':':
                self.advance()
                if self.current_char() == ':':
                    self.advance()
                    self.tokens.append(Token(TokenType.DOUBLE_COLON, '::', line, column))
                else:
                    self.tokens.append(Token(TokenType.COLON, ':', line, column))
            
            else:
                self.advance()
        
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens


if __name__ == "__main__":
    # اختبار الـ Lexer
    code = """
    let name: String = "نيكسو"
    let age: Int = 25
    
    func add(a: Int, b: Int) -> Int {
        return a + b
    }
    
    if age > 18 {
        print("بالغ")
    }
    """
    
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    
    for token in tokens:
        print(token)
