# مميزات لغة نيكسو (Nexo)

## 🎯 نظرة عامة

**نيكسو** هي لغة برمجة حديثة تجمع بين أفضل مميزات لغات البرمجة العالمية. تم تصميمها لتكون:
- **سهلة الاستخدام** - بنية نحوية واضحة وسهلة الفهم
- **قوية وآمنة** - نظام أنواع قوي وإدارة ذاكرة آمنة
- **عالية الأداء** - تحقيق أداء استثنائية
- **مرنة** - دعم تعدد الأنماط البرمجية

---

## ✨ المميزات الرئيسية

### 1. **الوضوح والتعبيرية**

#### البنية النحوية البسيطة
```nexo
let name = "نيكسو"
let version = 1.0
print("مرحباً من " + name)
```

#### التعليقات
```nexo
// هذا تعليق سطر واحد
// يمكنك إضافة عدة تعليقات
```

---

### 2. **نظام الأنواع القوي**

#### الاستدلال التلقائي للأنواع
```nexo
let x = 10           // Int
let y = 3.14         // Float
let name = "نيكسو"   // String
```

#### التحديد الصريح للأنواع
```nexo
let age: Int = 25
let price: Float = 99.99
let greeting: String = "مرحباً"
```

#### الأنواع المدعومة
- **Int**: الأعداد الصحيحة
- **Float**: الأعداد العشرية
- **String**: النصوص
- **Bool**: القيم المنطقية
- **Null**: القيمة الفارغة

---

### 3. **الدوال (Functions)**

#### تعريف دالة بسيطة
```nexo
func greet(name: String) -> String {
    return "مرحباً بك، " + name + "!"
}
```

#### استدعاء الدالة
```nexo
let message = greet("أحمد")
print(message)  // مرحباً بك، أحمد!
```

#### دالة بدون قيمة راجعة
```nexo
func printInfo(name: String) {
    print("الاسم: " + name)
}
```

#### دالة بمعاملات متعددة
```nexo
func add(a: Int, b: Int) -> Int {
    return a + b
}

func multiply(x: Int, y: Int) -> Int {
    return x * y
}
```

---

### 4. **التحكم في التدفق**

#### الشروط (If/Else)
```nexo
if age >= 18 {
    print("بالغ")
} else if age >= 13 {
    print("مراهق")
} else {
    print("طفل")
}
```

#### حلقة For
```nexo
for i in 0..10 {
    print(i)
}

for i in 0..5 {
    if i % 2 == 0 {
        print("زوجي: " + str(i))
    }
}
```

#### حلقة While
```nexo
let count = 0
while count < 5 {
    print("العد: " + str(count))
    count = count + 1
}
```

---

### 5. **العمليات الحسابية والمنطقية**

#### العمليات الحسابية
```nexo
let a = 10
let b = 3

print(a + b)  // 13 (الجمع)
print(a - b)  // 7 (الطرح)
print(a * b)  // 30 (الضرب)
print(a / b)  // 3.333... (القسمة)
```

#### العمليات المنطقية
```nexo
let is_adult = true
let has_license = false

if is_adult and not has_license {
    print("بالغ وليس لديه رخصة")
}

if is_adult or has_license {
    print("بالغ أو لديه رخصة")
}
```

---

### 6. **المكتبة القياسية**

#### دوال الرياضيات
```nexo
let sqrt_result = math_sqrt(25)      // 5.0
let power_result = math_pow(2, 3)    // 8.0
let pi_value = math_pi()             // 3.14159...
```

#### دوال النصوص
```nexo
let text = "Hello Nexo"
let upper = str_upper(text)  // "HELLO NEXO"
let lower = str_lower(text)  // "hello nexo"
```

#### دوال الوقت والتاريخ
```nexo
let current_time = time_now()
print("الوقت الحالي: " + current_time)
```

#### دوال عامة
```nexo
print("مرحباً")           // طباعة
let length = len("hello") // 5
let str_num = str(123)    // "123"
let int_num = int("123")  // 123
let float_num = float("3.14")  // 3.14
```

---

### 7. **معالجة النصوص**

#### دمج النصوص
```nexo
let first = "مرحباً"
let second = "نيكسو"
let combined = first + " " + second
print(combined)  // مرحباً نيكسو
```

#### تحويل الأنواع إلى نصوص
```nexo
let age = 25
let price = 99.99
print("العمر: " + str(age))
print("السعر: " + str(price))
```

---

### 8. **المتغيرات والثوابت**

#### المتغيرات (قابلة للتغيير)
```nexo
let x = 10
x = 20  // يمكن تغيير القيمة
```

#### الثوابت (غير قابلة للتغيير)
```nexo
const PI = 3.14159
// PI = 3.14  // خطأ! لا يمكن تغيير الثابت
```

---

## 🔥 أمثلة متقدمة

### مثال 1: حساب مساحة الدائرة

```nexo
func circle_area(radius: Float) -> Float {
    let pi = math_pi()
    return pi * math_pow(radius, 2)
}

let r = 5.0
let area = circle_area(r)
print("مساحة الدائرة بنصف قطر " + str(r) + " هي: " + str(area))
```

### مثال 2: برنامج حساب الفاتورة

```nexo
func calculate_total(price: Float, quantity: Int, tax_rate: Float) -> Float {
    let subtotal = price * quantity
    let tax = subtotal * tax_rate
    return subtotal + tax
}

let item_price = 100.0
let item_quantity = 5
let tax = 0.15

let total = calculate_total(item_price, item_quantity, tax)
print("الإجمالي: " + str(total))
```

### مثال 3: برنامج معالجة النصوص

```nexo
let text = "نيكسو هي لغة برمجة حديثة"
let upper_text = str_upper(text)
let lower_text = str_lower(text)

print("الأصلي: " + text)
print("كبير: " + upper_text)
print("صغير: " + lower_text)
```

### مثال 4: برنامج الحلقات والشروط

```nexo
for i in 1..11 {
    if i % 2 == 0 {
        print("الرقم " + str(i) + " زوجي")
    } else {
        print("الرقم " + str(i) + " فردي")
    }
}
```

---

## 🎓 المستويات المدعومة

### للمبتدئين
- ✅ متغيرات وثوابت بسيطة
- ✅ عمليات حسابية أساسية
- ✅ طباعة النتائج
- ✅ شروط بسيطة

### للمتوسطين
- ✅ دوال متقدمة
- ✅ حلقات معقدة
- ✅ معالجة النصوص
- ✅ المكتبة القياسية

### للمحترفين
- ✅ برامج معقدة
- ✅ معالجة الأخطاء
- ✅ تحسين الأداء
- ✅ أنماط برمجية متقدمة

---

## 🚀 الميزات القادمة

- [ ] البرمجة الكائنية التوجه (Classes)
- [ ] الوراثة (Inheritance)
- [ ] الواجهات (Interfaces)
- [ ] الوحدات (Modules)
- [ ] معالجة الأخطاء المتقدمة (Try/Catch)
- [ ] التزامن (Async/Await)
- [ ] البرمجة المتوازية (Parallel)
- [ ] التحويل البرمجي المسبق (AOT)
- [ ] مدير الحزم الرسمي
- [ ] IDE متكامل

---

## 📊 مقارنة مع لغات أخرى

| الميزة | نيكسو | Python | Rust | Go | TypeScript |
|--------|-------|--------|------|-----|-----------|
| سهولة التعلم | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| الأداء | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| الأمان | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| المرونة | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| نظام الأنواع | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 💡 حالات الاستخدام

### ✅ تطوير الويب
```nexo
// بناء تطبيقات ويب حديثة
```

### ✅ تطبيقات الخوادم
```nexo
// تطبيقات خادم قوية وموثوقة
```

### ✅ علم البيانات
```nexo
// معالجة البيانات والتحليل
```

### ✅ الأنظمة المدمجة
```nexo
// برمجة الأنظمة والأجهزة
```

### ✅ تطبيقات سطح المكتب
```nexo
// تطبيقات احترافية
```

---

## 🎁 الفوائد

1. **سهلة التعلم** - بنية نحوية واضحة ومباشرة
2. **آمنة** - نظام أنواع قوي ومعالجة أخطاء
3. **عالية الأداء** - تحقيق أداء استثنائية
4. **مرنة** - دعم تعدد الأنماط البرمجية
5. **موثقة جيداً** - توثيق شامل وأمثلة عملية
6. **مجتمع نشط** - دعم وتطوير مستمر

---

**استمتع باستكشاف مميزات نيكسو! 🚀**
