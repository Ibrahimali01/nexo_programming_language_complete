import re
import sys
import math
import datetime
import os

class AetherStdLib:
    @staticmethod
    def get_functions():
        return {
            'math_sqrt': math.sqrt,
            'math_pow': math.pow,
            'math_pi': lambda: math.pi,
            'time_now': lambda: datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'str_upper': lambda s: s.upper(),
            'str_lower': lambda s: s.lower(),
        }

class AetherInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {
            'print': print,
            'len': len,
            'str': str,
            'int': int,
            'float': float,
            'input': input,
        }
        self.functions.update(AetherStdLib.get_functions())

    def execute(self, code):
        lines = code.split('\n')
        for line in lines:
            line = line.strip()
            if not line or line.startswith('//'):
                continue
            
            try:
                # let x = 10
                match_let = re.match(r'let\s+(\w+)\s*=\s*(.*)', line)
                if match_let:
                    var_name = match_let.group(1)
                    value_expr = match_let.group(2)
                    self.variables[var_name] = self.evaluate(value_expr)
                    continue

                # print(...)
                match_print = re.match(r'print\((.*)\)', line)
                if match_print:
                    expr = match_print.group(1)
                    print(self.evaluate(expr))
                    continue

                # func_call(...)
                match_func_call = re.match(r'(\w+)\((.*)\)', line)
                if match_func_call:
                    func_name = match_func_call.group(1)
                    args_str = match_func_call.group(2)
                    args = [self.evaluate(arg.strip()) for arg in args_str.split(',') if arg.strip()]
                    if func_name in self.functions:
                        self.functions[func_name](*args)
                    else:
                        print(f"Error: Function '{func_name}' not found.")
                    continue
            except Exception as e:
                print(f"Runtime Error on line '{line}': {e}")

    def evaluate(self, expr):
        expr = expr.strip()
        
        # Strings
        if (expr.startswith('"') and expr.endswith('"')) or (expr.startswith("'") and expr.endswith("'")):
            return expr[1:-1]
        
        # Numbers
        try:
            if '.' in expr: return float(expr)
            return int(expr)
        except ValueError:
            pass
        
        # Variables
        if expr in self.variables:
            return self.variables[expr]
        
        # Function calls in expressions: math_sqrt(16)
        match_func = re.match(r'(\w+)\((.*)\)', expr)
        if match_func:
            func_name = match_func.group(1)
            args_str = match_func.group(2)
            args = [self.evaluate(arg.strip()) for arg in args_str.split(',') if arg.strip()]
            if func_name in self.functions:
                return self.functions[func_name](*args)

        # Basic Arithmetic (Simple parser)
        if '+' in expr:
            parts = expr.split('+', 1)
            return self.evaluate(parts[0]) + self.evaluate(parts[1])
        if '-' in expr:
            parts = expr.split('-', 1)
            return self.evaluate(parts[0]) - self.evaluate(parts[1])
        if '*' in expr:
            parts = expr.split('*', 1)
            return self.evaluate(parts[0]) * self.evaluate(parts[1])
        if '/' in expr:
            parts = expr.split('/', 1)
            return self.evaluate(parts[0]) / self.evaluate(parts[1])
        
        return expr

if __name__ == "__main__":
    interpreter = AetherInterpreter()
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            interpreter.execute(f.read())
    else:
        print("Aether Interpreter v1.0")
        print("Usage: python3 aether_interpreter.py <file.ae>")
