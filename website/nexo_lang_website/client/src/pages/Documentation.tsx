import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { ArrowLeft, ChevronRight } from "lucide-react";
import { useState } from "react";
import { useLocation } from "wouter";

const DOCS_SECTIONS = [
  {
    id: "intro",
    title: "مقدمة إلى نيكسو",
    content: `نيكسو (Nexo) هي لغة برمجة حديثة، متعددة الأنماط، وآمنة، مصممة لتوفير بيئة تطوير قوية ومرنة.

تجمع نيكسو بين:
• بساطة Python في القراءة والكتابة
• صرامة TypeScript في نظام الأنواع
• مميزات الأداء والأمان من Rust و Go

الأهداف الرئيسية:
1. الوضوح والتعبيرية
2. تعدد الأنماط البرمجية
3. الأمان والموثوقية
4. الأداء العالي
5. التزامن الأصيل
6. التوافقية مع اللغات الأخرى`
  },
  {
    id: "variables",
    title: "المتغيرات والأنواع",
    content: `تُعرف المتغيرات باستخدام الكلمة المفتاحية 'let':

let name: String = "نيكسو"     // متغير من نوع String
let age = 30                  // استدلال النوع كـ Int
const PI: Float = 3.14159    // ثابت

الأنواع الأساسية:
• Int: الأعداد الصحيحة (10, -5, 0)
• Float: الأعداد العشرية (3.14, -0.5)
• String: النصوص ("مرحباً", 'Hello')
• Bool: القيم المنطقية (true, false)
• Null: القيمة الفارغة (null)

يمكنك إعادة تعيين قيمة المتغيرات:
name = "لغة نيكسو"`
  },
  {
    id: "functions",
    title: "الدوال",
    content: `تُعرف الدوال باستخدام الكلمة المفتاحية 'func':

func greet(name: String) -> String {
    return "أهلاً بك، " + name + "!"
}

func add(a: Int, b: Int) -> Int {
    return a + b
}

let message = greet("العالم")
print(message)

let sum = add(10, 20)
print(sum)

خصائص الدوال:
• تحديد أنواع المعاملات
• تحديد نوع القيمة الراجعة
• إمكانية استدعاء الدوال من داخل الدوال
• دعم القيم الافتراضية (قيد التطوير)`
  },
  {
    id: "control",
    title: "التحكم في التدفق",
    content: `الشروط (If/Else):

if temperature > 30 {
    print("الجو حار جداً")
} else if temperature > 20 {
    print("الجو معتدل")
} else {
    print("الجو بارد")
}

حلقة for:

for i in 0..5 {
    print(i)
}

حلقة while:

let count = 0
while count < 3 {
    print("العد: " + str(count))
    count = count + 1
}

العمليات المنطقية:
• and: و المنطقية
• or: أو المنطقية
• not: النفي المنطقي`
  },
  {
    id: "stdlib",
    title: "المكتبة القياسية",
    content: `توفر أثير مكتبة قياسية غنية بالوظائف المدمجة:

وظائف الرياضيات:
• math_sqrt(number): الجذر التربيعي
• math_pow(base, exp): القوة
• math_pi(): قيمة باي

وظائف النصوص:
• str_upper(string): تحويل لأحرف كبيرة
• str_lower(string): تحويل لأحرف صغيرة

وظائف الوقت:
• time_now(): الوقت والتاريخ الحالي

وظائف عامة:
• print(value): طباعة قيمة
• len(value): طول السلسلة
• str(value): تحويل لنص
• int(value): تحويل لعدد صحيح
• float(value): تحويل لعدد عشري

أمثلة:
let result = math_sqrt(25)
print(result)  // 5.0

let text = "Hello"
print(str_upper(text))  // HELLO`
  },
  {
    id: "examples",
    title: "أمثلة عملية",
    content: `مثال 1: حساب مساحة الدائرة

let radius = 5
let pi = math_pi()
let area = pi * math_pow(radius, 2)
print("مساحة الدائرة: " + str(area))

مثال 2: عملية حسابية بسيطة

let x = 10
let y = 20
let sum = x + y
let product = x * y
print("المجموع: " + str(sum))
print("الضرب: " + str(product))

مثال 3: معالجة النصوص

let name = "نيكسو"
let upper = str_upper(name)
let lower = str_lower(name)
print("الأصلي: " + name)
print("كبير: " + upper)
print("صغير: " + lower)

مثال 4: الوقت والتاريخ

let current_time = time_now()
print("الوقت الحالي: " + current_time)`
  }
];

export default function Documentation() {
  const [, setLocation] = useLocation();
  const [selectedSection, setSelectedSection] = useState("intro");

  const currentSection = DOCS_SECTIONS.find(s => s.id === selectedSection);

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      {/* Header */}
      <div className="border-b border-slate-700/50 bg-slate-900/80 backdrop-blur-md sticky top-0 z-40">
        <div className="container py-4 flex items-center gap-4">
          <Button 
            onClick={() => setLocation("/")}
            variant="ghost"
            className="text-slate-300 hover:text-white"
          >
            <ArrowLeft className="w-5 h-5 mr-2" />
            العودة
          </Button>
          <h1 className="text-2xl font-bold text-white">توثيق نيكسو</h1>
        </div>
      </div>

      <div className="container py-8">
        <div className="grid lg:grid-cols-4 gap-8">
          {/* Sidebar */}
          <div className="lg:col-span-1">
            <div className="sticky top-24">
              <h3 className="text-lg font-bold text-white mb-4">الأقسام</h3>
              <div className="space-y-2">
                {DOCS_SECTIONS.map(section => (
                  <button
                    key={section.id}
                    onClick={() => setSelectedSection(section.id)}
                    className={`w-full text-right px-4 py-3 rounded-lg transition flex items-center justify-between ${
                      selectedSection === section.id
                        ? "bg-cyan-500/20 border border-cyan-500/50 text-cyan-400"
                        : "text-slate-300 hover:bg-slate-800/50"
                    }`}
                  >
                    <span>{section.title}</span>
                    {selectedSection === section.id && <ChevronRight className="w-4 h-4" />}
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Content */}
          <div className="lg:col-span-3">
            {currentSection && (
              <Card className="bg-slate-800/50 border-slate-700/50 p-8">
                <h2 className="text-3xl font-bold text-white mb-6">{currentSection.title}</h2>
                
                <div className="prose prose-invert max-w-none">
                  <pre className="bg-slate-900 rounded-lg p-6 overflow-x-auto text-sm text-slate-300 font-mono whitespace-pre-wrap break-words">
                    {currentSection.content}
                  </pre>
                </div>

                {/* Navigation */}
                <div className="flex gap-4 mt-8 pt-8 border-t border-slate-700/50">
                  {DOCS_SECTIONS.findIndex(s => s.id === selectedSection) > 0 && (
                    <Button 
                      onClick={() => {
                        const idx = DOCS_SECTIONS.findIndex(s => s.id === selectedSection);
                        setSelectedSection(DOCS_SECTIONS[idx - 1].id);
                      }}
                      variant="outline"
                      className="border-slate-600 text-slate-300 hover:bg-slate-800"
                    >
                      السابق
                    </Button>
                  )}
                  {DOCS_SECTIONS.findIndex(s => s.id === selectedSection) < DOCS_SECTIONS.length - 1 && (
                    <Button 
                      onClick={() => {
                        const idx = DOCS_SECTIONS.findIndex(s => s.id === selectedSection);
                        setSelectedSection(DOCS_SECTIONS[idx + 1].id);
                      }}
                      className="bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600"
                    >
                      التالي
                    </Button>
                  )}
                </div>
              </Card>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
