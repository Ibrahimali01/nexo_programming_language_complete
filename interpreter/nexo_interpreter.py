#!/usr/bin/env python3
"""
Nexo Programming Language - Full Interpreter
مترجم نيكسو الكامل - تنفيذ البرامج
"""

import sys
import os
import json
import math
import datetime
import subprocess
from typing import Any, Dict, List, Optional
from nexo_lexer import Lexer
from nexo_parser import (
    Parser, ASTNode, Program, VariableDeclaration, FunctionDeclaration,
    ClassDeclaration, IfStatement, ForLoop, WhileLoop, ReturnStatement,
    FunctionCall, BinaryOp, UnaryOp, Literal, Identifier, ListLiteral,
    MapLiteral, TryStatement, ThrowStatement, ImportStatement
)

class NexoException(Exception):
    pass

class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value

class BreakException(Exception):
    pass

class ContinueException(Exception):
    pass

class Environment:
    def __init__(self, parent: Optional['Environment'] = None):
        self.parent = parent
        self.variables: Dict[str, Any] = {}
    
    def define(self, name: str, value: Any):
        self.variables[name] = value
    
    def get(self, name: str) -> Any:
        if name in self.variables:
            return self.variables[name]
        if self.parent:
            return self.parent.get(name)
        raise NexoException(f"متغير غير معرّف: {name}")
    
    def set(self, name: str, value: Any):
        if name in self.variables:
            self.variables[name] = value
        elif self.parent:
            self.parent.set(name, value)
        else:
            self.variables[name] = value

class NexoFunction:
    def __init__(self, params: List[tuple], body: List[ASTNode], closure: Environment):
        self.params = params
        self.body = body
        self.closure = closure

class NexoClass:
    def __init__(self, name: str, methods: Dict[str, NexoFunction], parent: Optional['NexoClass'] = None):
        self.name = name
        self.methods = methods
        self.parent = parent
    
    def instantiate(self, *args):
        return NexoObject(self, args)

class NexoObject:
    def __init__(self, klass: NexoClass, init_args: tuple):
        self.klass = klass
        self.attributes: Dict[str, Any] = {}
        
        if 'constructor' in klass.methods:
            # استدعاء المُنشئ
            pass

class Interpreter:
    def __init__(self):
        self.global_env = Environment()
        self.setup_builtins()
    
    def setup_builtins(self):
        """إعداد الدوال والثوابت المدمجة"""
        
        # دوال الطباعة
        self.global_env.define('print', self.builtin_print)
        self.global_env.define('println', self.builtin_println)
        
        # دوال الرياضيات
        self.global_env.define('math_sqrt', lambda x: math.sqrt(x))
        self.global_env.define('math_pow', lambda x, y: math.pow(x, y))
        self.global_env.define('math_abs', lambda x: abs(x))
        self.global_env.define('math_sin', lambda x: math.sin(x))
        self.global_env.define('math_cos', lambda x: math.cos(x))
        self.global_env.define('math_tan', lambda x: math.tan(x))
        self.global_env.define('math_floor', lambda x: math.floor(x))
        self.global_env.define('math_ceil', lambda x: math.ceil(x))
        self.global_env.define('math_round', lambda x: round(x))
        self.global_env.define('math_min', lambda *args: min(args))
        self.global_env.define('math_max', lambda *args: max(args))
        self.global_env.define('math_pi', lambda: math.pi)
        self.global_env.define('math_e', lambda: math.e)
        self.global_env.define('math_random', lambda: __import__('random').random())
        
        # دوال النصوص
        self.global_env.define('str_upper', lambda s: str(s).upper())
        self.global_env.define('str_lower', lambda s: str(s).lower())
        self.global_env.define('str_length', lambda s: len(str(s)))
        self.global_env.define('str_trim', lambda s: str(s).strip())
        self.global_env.define('str_replace', lambda s, old, new: str(s).replace(old, new))
        self.global_env.define('str_split', lambda s, sep: str(s).split(sep))
        self.global_env.define('str_join', lambda lst, sep: sep.join(map(str, lst)))
        self.global_env.define('str_contains', lambda s, sub: sub in str(s))
        self.global_env.define('str_index', lambda s, sub: str(s).find(sub))
        self.global_env.define('str_substring', lambda s, start, end: str(s)[start:end])
        
        # دوال التحويل
        self.global_env.define('int', lambda x: int(x))
        self.global_env.define('float', lambda x: float(x))
        self.global_env.define('str', lambda x: str(x))
        self.global_env.define('bool', lambda x: bool(x))
        self.global_env.define('list', lambda x: list(x))
        
        # دوال الوقت
        self.global_env.define('time_now', lambda: datetime.datetime.now().isoformat())
        self.global_env.define('time_timestamp', lambda: int(__import__('time').time()))
        
        # دوال الملفات
        self.global_env.define('fs_read', self.builtin_fs_read)
        self.global_env.define('fs_write', self.builtin_fs_write)
        self.global_env.define('fs_exists', lambda path: os.path.exists(path))
        self.global_env.define('fs_delete', lambda path: os.remove(path))
        self.global_env.define('fs_mkdir', lambda path: os.makedirs(path, exist_ok=True))
        self.global_env.define('fs_list', lambda path: os.listdir(path))
        
        # دوال النظام
        self.global_env.define('os_execute', self.builtin_os_execute)
        self.global_env.define('os_getenv', lambda name: os.getenv(name))
        self.global_env.define('os_setenv', lambda name, value: os.environ.update({name: value}))
        
        # دوال JSON
        self.global_env.define('json_parse', lambda s: json.loads(s))
        self.global_env.define('json_stringify', lambda obj: json.dumps(obj))
        
        # دوال القوائم
        self.global_env.define('list_length', lambda lst: len(lst))
        self.global_env.define('list_push', lambda lst, item: lst.append(item) or lst)
        self.global_env.define('list_pop', lambda lst: lst.pop() if lst else None)
        self.global_env.define('list_shift', lambda lst: lst.pop(0) if lst else None)
        self.global_env.define('list_unshift', lambda lst, item: lst.insert(0, item) or lst)
        self.global_env.define('list_map', lambda lst, fn: [fn(x) for x in lst])
        self.global_env.define('list_filter', lambda lst, fn: [x for x in lst if fn(x)])
        self.global_env.define('list_reduce', lambda lst, fn, init: __import__('functools').reduce(fn, lst, init))
    
    def builtin_print(self, *args):
        print(' '.join(str(arg) for arg in args), end='')
        return None
    
    def builtin_println(self, *args):
        print(' '.join(str(arg) for arg in args))
        return None
    
    def builtin_fs_read(self, path: str) -> str:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            raise NexoException(f"خطأ في قراءة الملف: {e}")
    
    def builtin_fs_write(self, path: str, content: str):
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            raise NexoException(f"خطأ في كتابة الملف: {e}")
    
    def builtin_os_execute(self, command: str) -> str:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            raise NexoException(f"خطأ في تنفيذ الأمر: {e}")
    
    def interpret(self, source: str):
        """تفسير وتنفيذ الكود"""
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        return self.evaluate(ast, self.global_env)
    
    def evaluate(self, node: ASTNode, env: Environment) -> Any:
        if isinstance(node, Program):
            result = None
            for stmt in node.statements:
                result = self.evaluate(stmt, env)
            return result
        
        elif isinstance(node, VariableDeclaration):
            value = None
            if node.value:
                value = self.evaluate(node.value, env)
            env.define(node.name, value)
            return value
        
        elif isinstance(node, FunctionDeclaration):
            func = NexoFunction(node.parameters, node.body, env)
            env.define(node.name, func)
            return func
        
        elif isinstance(node, IfStatement):
            condition = self.evaluate(node.condition, env)
            if self.is_truthy(condition):
                result = None
                for stmt in node.then_body:
                    result = self.evaluate(stmt, env)
                return result
            elif node.else_body:
                result = None
                for stmt in node.else_body:
                    result = self.evaluate(stmt, env)
                return result
            return None
        
        elif isinstance(node, ForLoop):
            iterable = self.evaluate(node.iterable, env)
            result = None
            
            for item in iterable:
                loop_env = Environment(env)
                loop_env.define(node.variable, item)
                
                try:
                    for stmt in node.body:
                        result = self.evaluate(stmt, loop_env)
                except BreakException:
                    break
                except ContinueException:
                    continue
            
            return result
        
        elif isinstance(node, WhileLoop):
            result = None
            while self.is_truthy(self.evaluate(node.condition, env)):
                try:
                    for stmt in node.body:
                        result = self.evaluate(stmt, env)
                except BreakException:
                    break
                except ContinueException:
                    continue
            return result
        
        elif isinstance(node, ReturnStatement):
            value = None
            if node.value:
                value = self.evaluate(node.value, env)
            raise ReturnValue(value)
        
        elif isinstance(node, FunctionCall):
            func = env.get(node.name)
            args = [self.evaluate(arg, env) for arg in node.arguments]
            
            if isinstance(func, NexoFunction):
                call_env = Environment(func.closure)
                for (param_name, _), arg in zip(func.params, args):
                    call_env.define(param_name, arg)
                
                result = None
                try:
                    for stmt in func.body:
                        result = self.evaluate(stmt, call_env)
                except ReturnValue as ret:
                    result = ret.value
                
                return result
            elif callable(func):
                return func(*args)
            else:
                raise NexoException(f"{node.name} ليست دالة")
        
        elif isinstance(node, BinaryOp):
            left = self.evaluate(node.left, env)
            right = self.evaluate(node.right, env)
            
            if node.operator == '+':
                return left + right
            elif node.operator == '-':
                return left - right
            elif node.operator == '*':
                return left * right
            elif node.operator == '/':
                return left / right if isinstance(left, float) or isinstance(right, float) else left // right
            elif node.operator == '%':
                return left % right
            elif node.operator == '**':
                return left ** right
            elif node.operator == '==':
                return left == right
            elif node.operator == '!=':
                return left != right
            elif node.operator == '<':
                return left < right
            elif node.operator == '<=':
                return left <= right
            elif node.operator == '>':
                return left > right
            elif node.operator == '>=':
                return left >= right
            elif node.operator == '&&':
                return self.is_truthy(left) and self.is_truthy(right)
            elif node.operator == '||':
                return self.is_truthy(left) or self.is_truthy(right)
            elif node.operator == '..':
                return list(range(int(left), int(right)))
            elif node.operator == '[]':
                return left[int(right)]
            elif node.operator == '.':
                if isinstance(right, Identifier):
                    return getattr(left, right.name, None)
            else:
                raise NexoException(f"معامل غير معروف: {node.operator}")
        
        elif isinstance(node, UnaryOp):
            operand = self.evaluate(node.operand, env)
            
            if node.operator == '-':
                return -operand
            elif node.operator == '+':
                return +operand
            elif node.operator == '!':
                return not self.is_truthy(operand)
            else:
                raise NexoException(f"معامل أحادي غير معروف: {node.operator}")
        
        elif isinstance(node, Literal):
            return node.value
        
        elif isinstance(node, Identifier):
            return env.get(node.name)
        
        elif isinstance(node, ListLiteral):
            return [self.evaluate(elem, env) for elem in node.elements]
        
        elif isinstance(node, MapLiteral):
            result = {}
            for key, value in node.pairs:
                k = self.evaluate(key, env)
                v = self.evaluate(value, env)
                result[k] = v
            return result
        
        elif isinstance(node, TryStatement):
            try:
                result = None
                for stmt in node.try_body:
                    result = self.evaluate(stmt, env)
                return result
            except Exception as e:
                for exception_type, body in node.catch_clauses:
                    if exception_type == 'Error' or exception_type == type(e).__name__:
                        result = None
                        for stmt in body:
                            result = self.evaluate(stmt, env)
                        return result
                raise
        
        elif isinstance(node, ThrowStatement):
            exception = self.evaluate(node.exception, env)
            raise NexoException(str(exception))
        
        elif isinstance(node, ImportStatement):
            # معالجة الاستيراد
            pass
        
        else:
            raise NexoException(f"عقدة غير معروفة: {type(node)}")
    
    def is_truthy(self, value: Any) -> bool:
        if value is None or value is False:
            return False
        if value == 0 or value == "" or value == [] or value == {}:
            return False
        return True


def main():
    if len(sys.argv) < 2:
        print("استخدام: nexo <file.nexo>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            source = f.read()
        
        interpreter = Interpreter()
        interpreter.interpret(source)
    
    except FileNotFoundError:
        print(f"خطأ: لم يتم العثور على الملف {filename}")
        sys.exit(1)
    except Exception as e:
        print(f"خطأ: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
