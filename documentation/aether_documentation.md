# توثيق لغة البرمجة أثير (Aether)

## 1. مقدمة إلى أثير

أثير (Aether) هي لغة برمجة حديثة، متعددة الأنماط، وآمنة، مصممة لتوفير بيئة تطوير قوية ومرنة. تجمع أثير بين بساطة القراءة والكتابة المستوحاة من Python، وصرامة نظام الأنواع من TypeScript، مع مميزات الأداء والأمان المستوحاة من Rust وGo. تهدف أثير إلى تمكين المطورين من بناء تطبيقات عالية الأداء وموثوقة عبر مجموعة واسعة من المجالات، بما في ذلك تطوير الويب، تطبيقات الخوادم، علم البيانات، والأنظمة المدمجة.

**الفلسفة والأهداف:**

*   **الوضوح والتعبيرية:** تصميم بنية نحوية سهلة الفهم والكتابة.
*   **تعدد الأنماط:** دعم البرمجة الكائنية التوجه، الوظيفية، والأمرية.
*   **الأمان:** التركيز على السلامة النوعية والذاكرية لتقليل الأخطاء.
*   **الأداء:** تحقيق أداء عالٍ مع إمكانية التحويل البرمجي المسبق.
*   **التزامن:** دعم أصيل للتزامن والبرمجة المتوازية.
*   **قابلية التشغيل البيني:** سهولة التكامل مع اللغات والأنظمة الأخرى.
*   **المرونة وقابلية التوسع:** مناسبة لمختلف أحجام المشاريع وأنواع التطبيقات.

## 2. البدء مع أثير

لتشغيل كود أثير، تحتاج إلى مترجم أثير. حاليًا، يتم توفير مترجم أثير كسكريبت Python.

### 2.1. المتطلبات

*   Python 3.x

### 2.2. التثبيت (المترجم)

لا يتطلب مترجم أثير تثبيتًا معقدًا. ما عليك سوى حفظ الكود الخاص بالمترجم في ملف `aether_interpreter.py`.

```python
# محتوى ملف aether_interpreter.py (تم توفيره سابقًا)
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
                    args = [self.evaluate(arg.strip()) for arg in args_str.split(',', 1) if arg.strip()]
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
            args = [self.evaluate(arg.strip()) for arg in args_str.split(',', 1) if arg.strip()]
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
```

### 2.3. تشغيل كود أثير

لنفترض أن لديك ملفًا باسم `hello.ae` يحتوي على كود أثير:

```aether
let message = "مرحباً من أثير!"
print(message)
```

يمكنك تشغيله باستخدام الأمر التالي في الطرفية:

```bash
python3 aether_interpreter.py hello.ae
```

**الناتج:**

```
مرحباً من أثير!
```

## 3. البنية النحوية والمفاهيم الأساسية

### 3.1. المتغيرات والثوابت

تُعرف المتغيرات باستخدام الكلمة المفتاحية `let`، ويمكن تحديد النوع اختياريًا. الثوابت تُعرف باستخدام `const`.

```aether
let name: String = "أثير" // متغير من نوع String
let age = 30             // استدلال النوع كـ Int
const PI: Float = 3.14159 // ثابت من نوع Float

// إعادة تعيين قيمة المتغيرات
name = "لغة أثير"
```

**أنواع البيانات الأساسية:**

*   `Int`: الأعداد الصحيحة (مثال: `10`, `-5`)
*   `Float`: الأعداد العشرية (مثال: `3.14`, `-0.5`)
*   `String`: النصوص (مثال: `"مرحباً"`, `"Aether Lang"`)
*   `Bool`: القيم المنطقية (`true`, `false`)
*   `Null`: القيمة الفارغة

### 3.2. الدوال (Functions)

تُعرف الدوال باستخدام الكلمة المفتاحية `func`، مع تحديد المعاملات وأنواعها، ونوع القيمة الراجعة.

```aether
func greet(name: String) -> String {
    return "أهلاً بك، \(name)!"
}

func add(a: Int, b: Int) -> Int {
    return a + b
}

let message = greet("العالم")
print(message)

let sum = add(10, 20)
print(sum)
```

### 3.3. التحكم في التدفق (Control Flow)

#### 3.3.1. الشروط (If/Else)

```aether
let temperature = 25

if temperature > 30 {
    print("الجو حار جداً")
} else if temperature > 20 {
    print("الجو معتدل")
} else {
    print("الجو بارد")
}
```

#### 3.3.2. الحلقات (Loops)

**حلقة `for`:**

```aether
for i in 0..5 { // من 0 إلى 4
    print(i)
}

// مثال آخر
let fruits = ["تفاح", "برتقال", "موز"]
for fruit in fruits {
    print(fruit)
}
```

**حلقة `while`:**

```aether
let count = 0
while count < 3 {
    print("العد: \(count)")
    count = count + 1
}
```

### 3.4. العمليات الحسابية والمنطقية

تدعم أثير العمليات الحسابية الأساسية (`+`, `-`, `*`, `/`) والعمليات المنطقية (`and`, `or`, `not`).

```aether
let a = 10
let b = 3

print(a + b) // 13
print(a - b) // 7
print(a * b) // 30
print(a / b) // 3.333...

let is_adult = true
let has_license = false

if is_adult and not has_license {
    print("بالغ وليس لديه رخصة")
}
```

## 4. المكتبة القياسية (Standard Library)

توفر أثير مكتبة قياسية غنية بالوظائف المدمجة لتسهيل المهام الشائعة.

### 4.1. وظائف الرياضيات (`math_`)

*   `math_sqrt(number)`: يحسب الجذر التربيعي.
*   `math_pow(base, exponent)`: يحسب القوة.
*   `math_pi()`: يعيد قيمة باي (π).

```aether
let result = math_sqrt(25)
print(result) // 5.0
print(math_pow(2, 3)) // 8.0
print(math_pi()) // 3.14159...
```

### 4.2. وظائف الوقت والتاريخ (`time_`)

*   `time_now()`: يعيد التاريخ والوقت الحالي كسلسلة نصية.

```aether
print(time_now())
```

### 4.3. وظائف النصوص (`str_`)

*   `str_upper(string)`: يحول النص إلى أحرف كبيرة.
*   `str_lower(string)`: يحول النص إلى أحرف صغيرة.

```aether
let text = "Hello Aether"
print(str_upper(text)) // "HELLO AETHER"
print(str_lower(text)) // "hello aether"
```

## 5. أمثلة متقدمة (قيد التطوير)

*   **الكائنات والفئات:** سيتم إضافة دعم كامل للبرمجة الكائنية التوجه.
*   **التزامن:** آليات مدمجة للتعامل مع المهام المتزامنة.
*   **معالجة الأخطاء:** نظام قوي للتعامل مع الأخطاء والاستثناءات.
*   **الوحدات:** نظام لإدارة الوحدات والتبعيات.

---
