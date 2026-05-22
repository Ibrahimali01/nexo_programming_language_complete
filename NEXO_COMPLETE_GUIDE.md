# دليل لغة نيكسو (Nexo) الشامل

## 🎯 مقدمة عن نيكسو

**نيكسو (Nexo)** هي لغة برمجة ثورية **مستقلة تماماً** وشاملة تدعم جميع مجالات البرمجة الحديثة:

✅ تطوير الويب (Frontend + Backend)
✅ تطبيقات الموبايل (Android + iOS)
✅ ألعاب الفيديو ومحركات الألعاب
✅ تعلم الآلة وتحليل البيانات
✅ أنظمة التشغيل والبرمجة النظامية
✅ قواعس البيانات والخوادم
✅ معالجة النصوص والملفات
✅ أتمتة المهام والسيرفرات
✅ الشبكات والأمان

---

## 📋 المحتويات

1. [البدء السريع](#البدء-السريع)
2. [البنية النحوية](#البنية-النحوية)
3. [الأنواع والمتغيرات](#الأنواع-والمتغيرات)
4. [الدوال](#الدوال)
5. [البرمجة الكائنية](#البرمجة-الكائنية)
6. [معالجة الأخطاء](#معالجة-الأخطاء)
7. [المكتبة القياسية](#المكتبة-القياسية)
8. [الأمثلة العملية](#الأمثلة-العملية)

---

## البدء السريع

### التثبيت والتشغيل

```bash
# تثبيت نيكسو
nexo install

# إنشاء مشروع جديد
nexo create my_project

# تشغيل ملف
nexo run main.nexo

# بناء المشروع
nexo build

# نشر المشروع
nexo deploy
```

### أول برنامج

```nexo
print("مرحباً بك في نيكسو!\n")
```

---

## البنية النحوية

### التعليقات

```nexo
// تعليق سطر واحد

/* تعليق متعدد
   الأسطر */
```

### الفواصل والمحددات

```nexo
let x = 10;        // نقطة فاصلة
let y = 20         // اختيارية في نهاية السطر

{
    // كتلة برمجية
}

(x, y)             // قوسان
[1, 2, 3]          // أقواس مربعة
{"key": "value"}   // أقواس معقوفة
```

---

## الأنواع والمتغيرات

### الأنواع الأساسية

```nexo
// الأعداد الصحيحة
let age: Int = 25
let count: Int = 100

// الأعداد العشرية
let price: Float = 99.99
let pi: Float = 3.14159

// النصوص
let name: String = "أحمد"
let message: String = "مرحباً"

// القيم المنطقية
let isActive: Bool = true
let isValid: Bool = false

// القيمة الفارغة
let empty: Null = null
```

### تعريف المتغيرات

```nexo
// متغير قابل للتغيير
let x = 10
x = 20  // مسموح

// متغير ثابت
const PI = 3.14159
PI = 3.14  // خطأ!

// متغير ديناميكي
var counter = 0
counter = counter + 1
```

### الاستدلال على النوع

```nexo
let x = 10              // Int
let y = 3.14            // Float
let text = "Hello"      // String
let flag = true         // Bool
```

### الأنواع المركبة

```nexo
// القائمة
let numbers: List<Int> = [1, 2, 3, 4, 5]
let mixed: List<Any> = [1, "text", true]

// القاموس
let person: Map<String, Any> = {
    "name": "أحمد",
    "age": 30,
    "email": "ahmed@example.com"
}

// الصف (Tuple)
let pair: Tuple<String, Int> = ("name", 25)
```

---

## الدوال

### تعريف الدوال

```nexo
func add(a: Int, b: Int) -> Int {
    return a + b
}

func greet(name: String) -> String {
    return "مرحباً " + name
}

func printMessage(msg: String) -> Void {
    print(msg)
}
```

### استدعاء الدوال

```nexo
let result = add(10, 20)
let greeting = greet("أحمد")
printMessage("Hello World")
```

### القيم الافتراضية

```nexo
func greet(name: String = "العالم") -> String {
    return "مرحباً " + name
}

greet()           // "مرحباً العالم"
greet("أحمد")     // "مرحباً أحمد"
```

### عدد متغير من المعاملات

```nexo
func sum(...numbers: Int) -> Int {
    let total = 0
    for num in numbers {
        total = total + num
    }
    return total
}

sum(1, 2, 3, 4, 5)  // 15
```

### الدوال من الدرجة الأولى

```nexo
let multiply = func(a: Int, b: Int) -> Int {
    return a * b
}

let result = multiply(5, 3)  // 15
```

### الدوال العالية الرتبة

```nexo
func applyTwice(f: Function, x: Int) -> Int {
    return f(f(x))
}

let double = func(x: Int) -> Int {
    return x * 2
}

applyTwice(double, 5)  // 20
```

---

## التحكم في التدفق

### الشروط

```nexo
let age = 25

if age >= 18 {
    print("بالغ\n")
} else if age >= 13 {
    print("مراهق\n")
} else {
    print("طفل\n")
}
```

### حلقة for

```nexo
for i in 1..10 {
    print(i)
    print(" ")
}
```

### حلقة while

```nexo
let count = 0
while count < 5 {
    print(count)
    print(" ")
    count = count + 1
}
```

### حلقة foreach

```nexo
let items = [1, 2, 3, 4, 5]
for item in items {
    print(item)
    print(" ")
}
```

### switch

```nexo
let day = 3

switch day {
    case 1: print("الاثنين\n")
    case 2: print("الثلاثاء\n")
    case 3: print("الأربعاء\n")
    default: print("يوم آخر\n")
}
```

### break و continue

```nexo
for i in 1..10 {
    if i == 5 {
        break  // خروج من الحلقة
    }
    if i == 2 {
        continue  // الانتقال للتكرار التالي
    }
    print(i)
}
```

---

## البرمجة الكائنية

### تعريف الفئات

```nexo
class Person {
    let name: String
    let age: Int
    
    constructor(name: String, age: Int) {
        this.name = name
        this.age = age
    }
    
    func greet() -> String {
        return "مرحباً، أنا " + this.name
    }
    
    func getAge() -> Int {
        return this.age
    }
}
```

### إنشاء الكائنات

```nexo
let person = new Person("أحمد", 30)
print(person.greet())
print(person.getAge())
```

### الوراثة

```nexo
class Employee extends Person {
    let salary: Float
    
    constructor(name: String, age: Int, salary: Float) {
        super(name, age)
        this.salary = salary
    }
    
    func getSalary() -> Float {
        return this.salary
    }
}

let emp = new Employee("محمد", 28, 50000)
print(emp.greet())
print(emp.getSalary())
```

### الواجهات

```nexo
interface Animal {
    func makeSound() -> String
    func move() -> Void
}

class Dog implements Animal {
    func makeSound() -> String {
        return "Woof!"
    }
    
    func move() -> Void {
        print("Running...\n")
    }
}
```

### الدوال الثابتة

```nexo
class Math {
    static func add(a: Int, b: Int) -> Int {
        return a + b
    }
}

let result = Math.add(10, 20)
```

---

## معالجة الأخطاء

### محاولة-التقاط

```nexo
try {
    let result = divide(10, 0)
    print(result)
} catch DivisionByZeroError {
    print("لا يمكن القسمة على صفر\n")
} catch error {
    print("خطأ: " + error.message + "\n")
}
```

### رفع الاستثناءات

```nexo
func divide(a: Int, b: Int) -> Int throws {
    if b == 0 {
        throw new DivisionByZeroError("لا يمكن القسمة على صفر")
    }
    return a / b
}
```

### الاستثناءات المخصصة

```nexo
class CustomError extends Error {
    let code: Int
    
    constructor(message: String, code: Int) {
        super(message)
        this.code = code
    }
}
```

### finally

```nexo
try {
    // كود قد يرفع استثناء
} catch error {
    // معالجة الخطأ
} finally {
    // كود يتم تنفيذه دائماً
}
```

---

## المكتبة القياسية

### نظام الملفات

```nexo
import fs

// قراءة ملف
let content = fs.read("file.txt")

// كتابة ملف
fs.write("output.txt", "Hello World")

// إضافة محتوى
fs.append("log.txt", "New entry\n")

// التحقق من الوجود
if fs.exists("file.txt") {
    print("الملف موجود\n")
}

// حذف ملف
fs.delete("temp.txt")

// إنشاء مجلد
fs.mkdir("my_folder")

// قائمة الملفات
let files = fs.list(".")
for file in files {
    print(file)
}

// معلومات الملف
let info = fs.getInfo("file.txt")
print(info.size)
print(info.modified)
```

### معالجة النصوص

```nexo
import string

let text = "Hello World"

// تحويلات
let upper = string.toUpperCase(text)
let lower = string.toLowerCase(text)
let trimmed = string.trim(text)

// البحث والاستبدال
let result = string.replace(text, "World", "Nexo")
let contains = string.contains(text, "World")
let index = string.indexOf(text, "World")

// تقسيم ودمج
let parts = string.split(text, " ")
let joined = string.join(parts, "-")

// استخراج أجزاء
let substring = string.substring(text, 0, 5)
let length = string.length(text)

// التحقق من الأنماط
let isEmail = string.matches(email, "^[a-zA-Z0-9@.]+$")
```

### الرياضيات

```nexo
import math

let sqrt = math.sqrt(16)
let power = math.pow(2, 3)
let abs = math.abs(-5)
let min = math.min(3, 5)
let max = math.max(3, 5)

// الدوال المثلثية
let sine = math.sin(0)
let cosine = math.cos(0)

// الثوابت
let pi = math.PI
let e = math.E

// التقريب
let rounded = math.round(3.7)
let floor = math.floor(3.7)
let ceil = math.ceil(3.2)

// الأرقام العشوائية
let random = math.random()
let randomInt = math.randomInt(1, 100)
```

### التاريخ والوقت

```nexo
import datetime

let now = datetime.now()
let timestamp = datetime.timestamp()

// تنسيق التاريخ
let formatted = datetime.format(now, "yyyy-MM-dd HH:mm:ss")

// إضافة وطرح
let tomorrow = datetime.addDays(now, 1)
let nextMonth = datetime.addMonths(now, 1)
```

### قواعد البيانات

```nexo
import database

let db = database.connect("sqlite:///mydb.db")

// الاستعلامات
let result = db.query("SELECT * FROM users WHERE age > 18")

// الإدراج
db.insert("users", {
    "name": "أحمد",
    "age": 30,
    "email": "ahmed@example.com"
})

// التحديث
db.update("users", {"age": 31}, {"id": 1})

// الحذف
db.delete("users", {"id": 1})

// الإغلاق
db.close()
```

### الأمان والتشفير

```nexo
import crypto

// تجزئة كلمة المرور
let hash = crypto.hashPassword("mypassword")
let verified = crypto.verifyPassword("mypassword", hash)

// التشفير
let encrypted = crypto.encrypt("secret data", "key")
let decrypted = crypto.decrypt(encrypted, "key")

// توليد رموز
let token = crypto.generateToken(32)

// التجزئة
let md5 = crypto.hashMD5("data")
let sha256 = crypto.hashSHA256("data")
```

### JSON

```nexo
import json

// التحليل
let data = json.parse('{"name": "أحمد", "age": 30}')

// التحويل
let jsonStr = json.stringify(data)

// الطباعة الجميلة
let pretty = json.prettyPrint(data)
```

### القوائم

```nexo
import list

let numbers = [1, 2, 3, 4, 5]

let length = list.length(numbers)
list.push(numbers, 6)
let last = list.pop(numbers)

let doubled = list.map(numbers, func(x) -> x * 2)
let evens = list.filter(numbers, func(x) -> x % 2 == 0)
let sum = list.reduce(numbers, func(a, b) -> a + b, 0)
```

### نظام التشغيل

```nexo
import os

// تنفيذ أوامر
let output = os.execute("ls -la")

// متغيرات البيئة
let apiKey = os.getEnv("API_KEY")
os.setEnv("DEBUG", "true")

// المجلد الحالي
let dir = os.currentDir()
os.changeDir("/home")

// نظام التشغيل
let platform = os.platform()

// التوقف
os.sleep(2)
```

---

## الأمثلة العملية

### مثال 1: حساب مساحة الدائرة

```nexo
import math

func circleArea(radius: Float) -> Float {
    return math.PI * math.pow(radius, 2)
}

let r = 5
let area = circleArea(r)
print("مساحة الدائرة بنصف قطر ")
print(r)
print(" = ")
print(area)
print("\n")
```

### مثال 2: معالجة الملفات

```nexo
import fs
import string

// قراءة ملف
let content = fs.read("input.txt")

// معالجة المحتوى
let lines = string.split(content, "\n")
let processed = string.join(lines, " | ")

// كتابة النتيجة
fs.write("output.txt", processed)

print("تمت معالجة الملف بنجاح\n")
```

### مثال 3: تطبيق ويب بسيط

```nexo
import http
import json

let server = http.createServer(3000)

server.onRequest(func(request, response) {
    if request.path == "/" {
        response.send("Welcome to Nexo!\n")
    } else if request.path == "/api/users" {
        let users = [
            {"id": 1, "name": "أحمد"},
            {"id": 2, "name": "محمد"}
        ]
        response.json(users)
    } else {
        response.status(404).send("Not Found\n")
    }
})

server.start()
print("Server running on port 3000\n")
```

### مثال 4: قاعدة بيانات

```nexo
import database

let db = database.connect("sqlite:///users.db")

// إنشاء جدول
db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

// إدراج بيانات
db.insert("users", {"name": "أحمد", "age": 30})
db.insert("users", {"name": "محمد", "age": 25})

// الاستعلام
let users = db.query("SELECT * FROM users")
for user in users {
    print(user)
}

db.close()
```

---

## نظام البناء والنشر

### ملف الإعدادات (nexo.config)

```json
{
    "name": "my_project",
    "version": "1.0.0",
    "description": "My Nexo Project",
    "author": "Your Name",
    "target": "web",
    "entry": "main.nexo",
    "output": "dist/",
    "dependencies": {
        "http": "latest",
        "database": "latest",
        "crypto": "latest"
    },
    "devDependencies": {
        "test": "latest"
    }
}
```

### أوامر البناء

```bash
# بناء المشروع
nexo build

# تشغيل المشروع
nexo run

# تشغيل الاختبارات
nexo test

# نشر المشروع
nexo deploy

# تنظيف الملفات المؤقتة
nexo clean
```

---

## الخلاصة

**نيكسو** هي لغة برمجة حديثة وقوية وشاملة تدعم جميع مجالات البرمجة. مع مكتبتها القياسية الضخمة وبنيتها النحوية الواضحة، تجعل البرمجة أسهل وأكثر متعة.

---

## الموارد الإضافية

- [الموقع الرسمي](https://nexo-lang.dev)
- [المستودع على GitHub](https://github.com/nexo-lang)
- [المنتدى](https://forum.nexo-lang.dev)
- [الدعم](https://support.nexo-lang.dev)

---

**صُنعت بـ ❤️ لمستقبل البرمجة**

**نيكسو - لغة البرمجة المستقبلية**
