import math
import datetime
import os

class AetherStdLib:
    @staticmethod
    def get_functions():
        return {
            # الرياضيات
            'math_sqrt': math.sqrt,
            'math_pow': math.pow,
            'math_sin': math.sin,
            'math_cos': math.cos,
            'math_pi': lambda: math.pi,
            
            # الوقت والتاريخ
            'time_now': lambda: datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            
            # النظام والملفات
            'sys_platform': lambda: os.name,
            'file_exists': os.path.exists,
            
            # معالجة النصوص
            'str_upper': lambda s: s.upper(),
            'str_lower': lambda s: s.lower(),
            'str_split': lambda s, d: s.split(d),
        }
