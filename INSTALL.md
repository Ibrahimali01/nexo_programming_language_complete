# دليل التثبيت والإعداد - لغة نيكسو

## 📋 المتطلبات الأساسية

### للمترجم:
- **Python 3.6+** أو أحدث
- نظام تشغيل: Windows, macOS, Linux

### للموقع الإلكتروني:
- **Node.js 22.x** أو أحدث
- **pnpm** (مدير الحزم)
- متصفح ويب حديث

---

## 🚀 خطوات التثبيت

### الخطوة 1: التحقق من المتطلبات

#### التحقق من Python:
```bash
python3 --version
# يجب أن تكون النتيجة 3.6 أو أحدث
```

#### التحقق من Node.js:
```bash
node --version
npm --version
```

#### تثبيت pnpm (إذا لم يكن مثبتاً):
```bash
npm install -g pnpm
pnpm --version
```

---

### الخطوة 2: استخراج الملفات

```bash
# استخرج ملف ZIP
unzip nexo_programming_language_complete.zip

# انتقل إلى المجلد
cd nexo_complete
```

---

### الخطوة 3: إعداد المترجم

```bash
# انتقل إلى مجلد المترجم
cd interpreter/

# تحقق من وجود الملفات
ls -la
# يجب أن ترى:
# - aether_interpreter.py
# - aether_stdlib.py
# - test.ae
# - advanced_test.ae
```

---

### الخطوة 4: إعداد الموقع الإلكتروني

```bash
# انتقل إلى مجلد الموقع
cd ../website/nexo_lang_website/

# تثبيت التبعيات
pnpm install

# قد يستغرق هذا عدة دقائق...
```

---

## ✅ التحقق من التثبيت

### اختبار المترجم:

```bash
cd interpreter/
python3 aether_interpreter.py test.ae
```

**الناتج المتوقع:**
```
أهلاً بالعالم
مجموع 5 + 10 هو:
15
```

### اختبار الموقع الإلكتروني:

```bash
cd website/nexo_lang_website/
pnpm dev
```

**الناتج المتوقع:**
```
VITE v7.1.9  ready in XXX ms

➜  Local:   http://localhost:3000/
➜  Network: http://xxx.xxx.xxx.xxx:3000/
```

---

## 🎯 الاستخدام الأساسي

### تشغيل برنامج نيكسو:

```bash
cd interpreter/
python3 aether_interpreter.py your_file.ae
```

### تشغيل الموقع الإلكتروني:

```bash
cd website/nexo_lang_website/
pnpm dev
```

ثم افتح المتصفح على: `http://localhost:3000`

---

## 🔧 استكشاف الأخطاء والمشاكل

### المشكلة: "command not found: python3"

**الحل:**
```bash
# تحقق من تثبيت Python
python --version

# أو استخدم python بدلاً من python3
python aether_interpreter.py test.ae
```

### المشكلة: "command not found: pnpm"

**الحل:**
```bash
# تثبيت pnpm
npm install -g pnpm

# تحقق من التثبيت
pnpm --version
```

### المشكلة: "Port 3000 already in use"

**الحل:**
```bash
# استخدم منفذ مختلف
pnpm dev -- --port 3001
```

### المشكلة: "Module not found"

**الحل:**
```bash
# أعد تثبيت التبعيات
cd website/nexo_lang_website/
rm -rf node_modules pnpm-lock.yaml
pnpm install
```

---

## 📁 هيكل المجلدات

```
nexo_complete/
├── README.md                    # دليل شامل
├── QUICKSTART.md               # دليل البدء السريع
├── FEATURES.md                 # مميزات اللغة
├── INSTALL.md                  # هذا الملف
├── language/
│   └── language_design.md      # تصميم اللغة
├── interpreter/
│   ├── aether_interpreter.py   # المترجم
│   ├── aether_stdlib.py        # المكتبة القياسية
│   ├── test.ae                 # اختبار بسيط
│   └── advanced_test.ae        # اختبار متقدم
├── documentation/
│   └── aether_documentation.md # التوثيق الكامل
└── website/
    └── nexo_lang_website/      # الموقع الإلكتروني
        ├── client/             # الواجهة الأمامية
        ├── server/             # الخادم
        ├── package.json        # التبعيات
        └── ...
```

---

## 🌐 الإعدادات المتقدمة

### تغيير منفذ الموقع:

```bash
cd website/nexo_lang_website/
pnpm dev -- --port 8080
```

### بناء الموقع للإنتاج:

```bash
cd website/nexo_lang_website/
pnpm build
```

### معاينة الموقع المبني:

```bash
pnpm preview
```

---

## 📚 الموارد الإضافية

- **التوثيق الكامل:** `documentation/aether_documentation.md`
- **دليل البدء السريع:** `QUICKSTART.md`
- **مميزات اللغة:** `FEATURES.md`
- **تصميم اللغة:** `language/language_design.md`

---

## 💡 نصائح مفيدة

1. **استخدم محرر نصوص جيد** مثل VS Code أو Sublime Text
2. **اقرأ التوثيق** قبل البدء
3. **جرب الأمثلة** أولاً قبل كتابة برامج معقدة
4. **استخدم المحرر التفاعلي** لاختبار الكود بسرعة
5. **احفظ عملك بانتظام** في ملفات منفصلة

---

## 🆘 الدعم

إذا واجهت مشاكل:

1. تحقق من هذا الدليل
2. اقرأ رسائل الخطأ بعناية
3. جرب الأمثلة المرفقة
4. اطلب المساعدة من المجتمع

---

## ✨ الخطوات التالية

بعد التثبيت الناجح:

1. ✅ اقرأ `QUICKSTART.md`
2. ✅ جرب الأمثلة في `interpreter/`
3. ✅ استكشف الموقع الإلكتروني
4. ✅ اقرأ التوثيق الكامل
5. ✅ اكتب برنامجك الأول

---

**مرحباً بك في عالم نيكسو! 🚀**
