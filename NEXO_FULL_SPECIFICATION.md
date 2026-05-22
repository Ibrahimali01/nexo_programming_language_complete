# لغة نيكسو (Nexo) - المواصفات الكاملة

## 🎯 رؤية اللغة

لغة برمجة **مستقلة تماماً** وشاملة تدعم جميع مجالات البرمجة الحديثة:
- تطوير الويب (Frontend + Backend)
- تطبيقات الموبايل (Android + iOS)
- ألعاب الفيديو ومحركات الألعاب
- تعلم الآلة وتحليل البيانات
- أنظمة التشغيل والبرمجة النظامية
- قواعد البيانات والخوادم
- معالجة النصوص والملفات
- أتمتة المهام والسيرفرات
- الشبكات والأمان

---

## 📋 البنية النحوية الأساسية

### 1. المتغيرات والأنواع

```nexo
// الأنواع الأساسية
let name: String = "نيكسو"
let age: Int = 25
let price: Float = 99.99
let active: Bool = true
let data: Null = null

// استدلال النوع
let x = 10              // Int
let y = 3.14            // Float
let text = "Hello"      // String

// الثوابت
const PI: Float = 3.14159
const MAX_SIZE: Int = 1000

// المتغيرات القابلة للتغيير
var counter = 0
counter = counter + 1

// الأنواع المركبة
let list: List<Int> = [1, 2, 3, 4, 5]
let map: Map<String, Int> = {"age": 25, "year": 2026}
let tuple: Tuple<String, Int> = ("name", 25)
```

### 2. الدوال والتحكم في التدفق

```nexo
// دالة بسيطة
func add(a: Int, b: Int) -> Int {
    return a + b
}

// دالة بدون قيمة راجعة
func printMessage(msg: String) -> Void {
    print(msg)
}

// دالة بقيم افتراضية
func greet(name: String = "العالم") -> String {
    return "مرحباً " + name
}

// دالة بعدد متغير من المعاملات
func sum(...numbers: Int) -> Int {
    let total = 0
    for num in numbers {
        total = total + num
    }
    return total
}

// الشروط
if age > 18 {
    print("بالغ")
} else if age > 13 {
    print("مراهق")
} else {
    print("طفل")
}

// حلقة for
for i in 0..10 {
    print(i)
}

// حلقة while
let count = 0
while count < 5 {
    print(count)
    count = count + 1
}

// حلقة foreach
for item in list {
    print(item)
}

// switch
switch day {
    case 1: print("الاثنين")
    case 2: print("الثلاثاء")
    default: print("يوم آخر")
}
```

### 3. البرمجة الكائنية التوجه

```nexo
// تعريف فئة
class Person {
    let name: String
    let age: Int
    
    // المُنشئ
    constructor(name: String, age: Int) {
        this.name = name
        this.age = age
    }
    
    // دالة عضو
    func greet() -> String {
        return "مرحباً، أنا " + this.name
    }
    
    // دالة ثابتة
    static func createDefault() -> Person {
        return new Person("Unknown", 0)
    }
}

// استخدام الفئة
let person = new Person("أحمد", 30)
print(person.greet())

// الوراثة
class Employee extends Person {
    let salary: Float
    
    constructor(name: String, age: Int, salary: Float) {
        super(name, age)
        this.salary = salary
    }
}

// الواجهات
interface Animal {
    func makeSound() -> String
    func move() -> Void
}

class Dog implements Animal {
    func makeSound() -> String {
        return "Woof!"
    }
    
    func move() -> Void {
        print("Running...")
    }
}
```

### 4. معالجة الأخطاء

```nexo
// محاولة-التقاط
try {
    let result = divide(10, 0)
    print(result)
} catch DivisionByZeroError {
    print("لا يمكن القسمة على صفر")
} catch error {
    print("خطأ: " + error.message)
}

// رفع استثناء
func divide(a: Int, b: Int) -> Int throws {
    if b == 0 {
        throw new DivisionByZeroError("لا يمكن القسمة على صفر")
    }
    return a / b
}

// تعريف استثناء مخصص
class CustomError extends Error {
    let code: Int
    
    constructor(message: String, code: Int) {
        super(message)
        this.code = code
    }
}
```

### 5. البرمجة الوظيفية

```nexo
// دوال من الدرجة الأولى
let multiply = func(a: Int, b: Int) -> Int {
    return a * b
}

// دوال عالية الرتبة
func applyTwice(f: Function, x: Int) -> Int {
    return f(f(x))
}

// Lambda/Arrow functions
let square = (x: Int) -> x * x
let add = (a: Int, b: Int) -> a + b

// Map, Filter, Reduce
let numbers = [1, 2, 3, 4, 5]
let doubled = numbers.map((x) -> x * 2)
let evens = numbers.filter((x) -> x % 2 == 0)
let sum = numbers.reduce(0, (acc, x) -> acc + x)

// Closures
func makeCounter() -> Function {
    let count = 0
    return func() -> Int {
        count = count + 1
        return count
    }
}
```

---

## 🔧 المكتبة القياسية الشاملة

### 1. نظام الملفات

```nexo
import fs

// قراءة ملف
let content = fs.readFile("file.txt")
print(content)

// كتابة ملف
fs.writeFile("output.txt", "Hello World")

// إنشاء مجلد
fs.createDirectory("my_folder")

// حذف ملف
fs.deleteFile("file.txt")

// قائمة الملفات
let files = fs.listFiles(".")
for file in files {
    print(file)
}

// التحقق من وجود ملف
if fs.exists("file.txt") {
    print("الملف موجود")
}

// الحصول على معلومات الملف
let info = fs.getFileInfo("file.txt")
print(info.size)
print(info.modified)
```

### 2. معالجة النصوص

```nexo
import string

let text = "Hello World"

// تحويلات النصوص
let upper = string.toUpperCase(text)
let lower = string.toLowerCase(text)
let trimmed = string.trim(text)

// البحث والاستبدال
let result = string.replace(text, "World", "Nexo")
let index = string.indexOf(text, "World")
let contains = string.contains(text, "World")

// تقسيم ودمج
let parts = string.split(text, " ")
let joined = string.join(parts, "-")

// استخراج أجزاء
let substring = string.substring(text, 0, 5)
let length = string.length(text)

// التحقق من الأنماط
let isEmail = string.matches(email, "^[a-zA-Z0-9@.]+$")
```

### 3. الرياضيات

```nexo
import math

// العمليات الأساسية
let sqrt = math.sqrt(16)          // 4.0
let power = math.pow(2, 3)        // 8
let abs = math.abs(-5)            // 5
let min = math.min(3, 5)          // 3
let max = math.max(3, 5)          // 5

// الدوال المثلثية
let sine = math.sin(0)
let cosine = math.cos(0)
let tangent = math.tan(0)

// الثوابت
let pi = math.PI
let e = math.E

// التقريب
let rounded = math.round(3.7)     // 4
let floor = math.floor(3.7)       // 3
let ceil = math.ceil(3.2)         // 4

// الأرقام العشوائية
let random = math.random()        // 0-1
let randomInt = math.randomInt(1, 100)
```

### 4. التاريخ والوقت

```nexo
import datetime

// الوقت الحالي
let now = datetime.now()
print(now)

// إنشاء تاريخ
let date = datetime.create(2026, 5, 22)

// تنسيق التاريخ
let formatted = datetime.format(now, "yyyy-MM-dd HH:mm:ss")

// حساب الفرق
let diff = datetime.difference(date1, date2)

// إضافة وطرح
let tomorrow = datetime.addDays(now, 1)
let nextMonth = datetime.addMonths(now, 1)

// استخراج أجزاء
let year = datetime.getYear(now)
let month = datetime.getMonth(now)
let day = datetime.getDay(now)
```

### 5. قواعد البيانات

```nexo
import database

// الاتصال بقاعدة البيانات
let db = database.connect("mysql://user:pass@localhost/mydb")

// تنفيذ استعلام
let result = db.query("SELECT * FROM users WHERE age > 18")

// إدراج بيانات
db.insert("users", {
    "name": "أحمد",
    "age": 30,
    "email": "ahmed@example.com"
})

// تحديث بيانات
db.update("users", {"age": 31}, {"id": 1})

// حذف بيانات
db.delete("users", {"id": 1})

// إغلاق الاتصال
db.close()
```

### 6. الشبكات والـ HTTP

```nexo
import http
import json

// طلب HTTP
let response = http.get("https://api.example.com/users")
let data = json.parse(response.body)

// إرسال بيانات
let payload = json.stringify({
    "name": "أحمد",
    "age": 30
})
let result = http.post("https://api.example.com/users", payload)

// خادم HTTP
let server = http.createServer(8080)
server.onRequest(func(request, response) {
    if request.path == "/hello" {
        response.send("Hello World")
    } else {
        response.status(404).send("Not Found")
    }
})
server.start()
```

### 7. تعلم الآلة وتحليل البيانات

```nexo
import ml
import data

// تحميل البيانات
let dataset = data.loadCSV("data.csv")

// معالجة البيانات
let normalized = data.normalize(dataset)
let features = data.selectColumns(dataset, ["age", "salary"])

// بناء نموذج
let model = ml.createLinearRegression()
model.train(features, labels)

// التنبؤ
let prediction = model.predict([30, 50000])

// تقييم النموذج
let accuracy = model.evaluate(testFeatures, testLabels)
print("الدقة: " + accuracy)

// شبكة عصبية
let nn = ml.createNeuralNetwork([10, 5, 1])
nn.train(trainingData, epochs=100)
let result = nn.predict(input)
```

### 8. الرسومات والألعاب

```nexo
import graphics
import game

// إنشاء نافذة
let window = graphics.createWindow(800, 600, "My Game")

// رسم أشكال
graphics.drawRectangle(100, 100, 50, 50, "red")
graphics.drawCircle(200, 200, 30, "blue")
graphics.drawLine(0, 0, 100, 100, "green")
graphics.drawText(50, 50, "Hello", "black")

// معالجة الأحداث
window.onKeyPress(func(key) {
    if key == "space" {
        print("Space pressed")
    }
})

// حلقة اللعبة
game.onUpdate(func() {
    // تحديث الحالة
})

game.onRender(func() {
    // رسم الإطار
})

game.start()
```

### 9. أتمتة المهام والسيرفرات

```nexo
import os
import scheduler

// تنفيذ أوامر النظام
let output = os.execute("ls -la")
print(output)

// إنشاء عملية
let process = os.spawn("python", ["script.py"])
process.wait()

// جدولة المهام
scheduler.schedule("0 0 * * *", func() {
    print("تشغيل يومي في منتصف الليل")
})

// مراقبة الملفات
os.watchFile("config.txt", func() {
    print("تم تعديل الملف!")
})

// متغيرات البيئة
let apiKey = os.getEnv("API_KEY")
os.setEnv("DEBUG", "true")
```

### 10. الأمان والتشفير

```nexo
import crypto
import security

// تجزئة كلمة المرور
let hash = crypto.hashPassword("mypassword")
let verified = crypto.verifyPassword("mypassword", hash)

// التشفير
let encrypted = crypto.encrypt("secret data", "key")
let decrypted = crypto.decrypt(encrypted, "key")

// توليد مفاتيح
let token = security.generateToken(32)

// التوقيع الرقمي
let signature = crypto.sign("message", privateKey)
let valid = crypto.verify("message", signature, publicKey)
```

---

## 🚀 أمثلة تطبيقات

### تطبيق ويب كامل

```nexo
import http
import database
import json

let db = database.connect("mysql://user:pass@localhost/blog")

let server = http.createServer(3000)

server.onRequest(func(request, response) {
    if request.method == "GET" && request.path == "/posts" {
        let posts = db.query("SELECT * FROM posts")
        response.json(posts)
    } else if request.method == "POST" && request.path == "/posts" {
        let data = json.parse(request.body)
        db.insert("posts", data)
        response.status(201).json({"success": true})
    }
})

server.start()
print("Server running on port 3000")
```

### تطبيق موبايل

```nexo
import mobile
import ui

let app = mobile.createApp("MyApp")

let mainScreen = ui.createScreen()
let button = ui.createButton("Click Me")
let label = ui.createLabel("Hello")

button.onClick(func() {
    label.setText("Button Clicked!")
})

mainScreen.add(button)
mainScreen.add(label)

app.setMainScreen(mainScreen)
app.run()
```

### لعبة بسيطة

```nexo
import game
import graphics
import math

let window = graphics.createWindow(800, 600, "Simple Game")

let playerX = 400
let playerY = 300
let speed = 5

game.onUpdate(func() {
    if game.isKeyPressed("left") {
        playerX = playerX - speed
    }
    if game.isKeyPressed("right") {
        playerX = playerX + speed
    }
})

game.onRender(func() {
    graphics.clear("white")
    graphics.drawRectangle(playerX, playerY, 50, 50, "blue")
})

game.start()
```

---

## 📦 نظام الحزم والمكتبات

```nexo
// تثبيت حزمة
nexo install package_name

// استيراد حزمة
import package_name

// إنشاء حزمة
nexo create-package my_package

// نشر حزمة
nexo publish my_package
```

---

## 🔄 نظام البناء والتجميع

```nexo
// ملف nexo.config
{
    "name": "my_project",
    "version": "1.0.0",
    "target": "web",
    "entry": "main.nexo",
    "output": "dist/",
    "dependencies": {
        "http": "latest",
        "database": "latest"
    }
}

// الأوامر
nexo build              // بناء المشروع
nexo run               // تشغيل المشروع
nexo test              // تشغيل الاختبارات
nexo deploy            // نشر المشروع
```

---

هذه هي مواصفات لغة **نيكسو (Nexo)** الكاملة والمستقلة تماماً!
