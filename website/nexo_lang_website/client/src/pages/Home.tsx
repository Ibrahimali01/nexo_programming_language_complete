import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Code2, Zap, Shield, Layers, BookOpen, Play } from "lucide-react";
import { useState } from "react";
import { useLocation } from "wouter";

export default function Home() {
  const [, setLocation] = useLocation();

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      {/* Navigation */}
      <nav className="fixed top-0 w-full bg-slate-900/80 backdrop-blur-md border-b border-slate-700/50 z-50">
        <div className="container flex items-center justify-between py-4">
          <div className="flex items-center gap-2">
            <div className="w-10 h-10 bg-gradient-to-br from-cyan-400 to-blue-500 rounded-lg flex items-center justify-center">
              <Code2 className="w-6 h-6 text-white" />
            </div>
            <span className="text-xl font-bold text-white">Nexo</span>
          </div>
          <div className="hidden md:flex items-center gap-8">
            <a href="#features" className="text-slate-300 hover:text-white transition">المميزات</a>
            <a href="#docs" className="text-slate-300 hover:text-white transition">التوثيق</a>
            <a href="#editor" className="text-slate-300 hover:text-white transition">المحرر</a>
            <Button 
              onClick={() => setLocation("/editor")}
              className="bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600"
            >
              ابدأ الآن
            </Button>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-4">
        <div className="container max-w-4xl mx-auto text-center">
          <div className="mb-6 inline-block">
            <span className="px-4 py-2 bg-cyan-500/10 border border-cyan-500/30 rounded-full text-cyan-400 text-sm font-medium">
              لغة برمجة ثورية
            </span>
          </div>
          
          <h1 className="text-5xl md:text-7xl font-bold text-white mb-6 leading-tight">
            نيكسو: لغة البرمجة المستقبلية
          </h1>
          
          <p className="text-xl text-slate-300 mb-12 max-w-2xl mx-auto leading-relaxed">
            تجمع نيكسو بين بساطة Python وقوة Rust وأداء Go. لغة برمجة حديثة متعددة الأنماط مصممة للمستقبل
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center mb-16">
            <Button 
              onClick={() => setLocation("/editor")}
              className="px-8 py-6 bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600 text-white text-lg rounded-lg"
            >
              <Play className="w-5 h-5 mr-2" />
              جرب الآن
            </Button>
            <Button 
              onClick={() => setLocation("/docs")}
              variant="outline"
              className="px-8 py-6 border-slate-600 text-white hover:bg-slate-800 text-lg rounded-lg"
            >
              <BookOpen className="w-5 h-5 mr-2" />
              اقرأ التوثيق
            </Button>
          </div>

          {/* Code Example */}
          <div className="bg-slate-800/50 border border-slate-700/50 rounded-xl p-6 backdrop-blur-sm">
            <pre className="text-left text-sm text-slate-300 font-mono overflow-x-auto">
{`let greeting = "مرحباً بك في نيكسو!"
let version = 1.0
print(greeting)
print("الإصدار: " + str(version))`}
            </pre>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20 px-4 border-t border-slate-700/50">
        <div className="container">
          <h2 className="text-4xl font-bold text-white mb-16 text-center">المميزات الرئيسية</h2>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {[
              {
                icon: Zap,
                title: "أداء عالي",
                description: "تحقيق أداء استثنائية مع إمكانية التحويل البرمجي المسبق"
              },
              {
                icon: Shield,
                title: "أمان قوي",
                description: "نظام أنواع ثابت وإدارة ذاكرة آمنة لتقليل الأخطاء"
              },
              {
                icon: Layers,
                title: "تعدد الأنماط",
                description: "دعم البرمجة الكائنية والوظيفية والأمرية"
              },
              {
                icon: Code2,
                title: "سهولة الاستخدام",
                description: "بنية نحوية واضحة وسهلة القراءة مستوحاة من Python"
              },
              {
                icon: Zap,
                title: "التزامن الأصيل",
                description: "دعم مدمج للبرمجة المتزامنة والمتوازية"
              },
              {
                icon: Shield,
                title: "التوافقية",
                description: "سهولة التكامل مع اللغات والأنظمة الأخرى"
              }
            ].map((feature, idx) => (
              <Card key={idx} className="bg-slate-800/50 border-slate-700/50 p-6 hover:border-cyan-500/50 transition">
                <feature.icon className="w-12 h-12 text-cyan-400 mb-4" />
                <h3 className="text-xl font-bold text-white mb-3">{feature.title}</h3>
                <p className="text-slate-400">{feature.description}</p>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Docs Preview Section */}
      <section id="docs" className="py-20 px-4 border-t border-slate-700/50">
        <div className="container">
          <h2 className="text-4xl font-bold text-white mb-16 text-center">ابدأ التعلم</h2>
          
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div>
              <h3 className="text-2xl font-bold text-white mb-6">توثيق شامل وسهل الفهم</h3>
              <p className="text-slate-300 mb-6 leading-relaxed">
                توفر نيكسو توثيقًا كاملاً يغطي جميع جوانب اللغة، من المفاهيم الأساسية إلى المواضيع المتقدمة. كل قسم يتضمن أمثلة عملية وشروحات مفصلة.
              </p>
              <ul className="space-y-3 text-slate-300">
                <li className="flex items-center gap-3">
                  <span className="w-2 h-2 bg-cyan-400 rounded-full"></span>
                  المتغيرات والأنواع
                </li>
                <li className="flex items-center gap-3">
                  <span className="w-2 h-2 bg-cyan-400 rounded-full"></span>
                  الدوال والتحكم في التدفق
                </li>
                <li className="flex items-center gap-3">
                  <span className="w-2 h-2 bg-cyan-400 rounded-full"></span>
                  البرمجة الكائنية التوجه
                </li>
                <li className="flex items-center gap-3">
                  <span className="w-2 h-2 bg-cyan-400 rounded-full"></span>
                  المكتبة القياسية
                </li>
              </ul>
              <Button 
                onClick={() => setLocation("/docs")}
                className="mt-8 bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600"
              >
                اقرأ التوثيق الكامل
              </Button>
            </div>
            
            <div className="bg-slate-800/50 border border-slate-700/50 rounded-xl p-8 backdrop-blur-sm">
              <pre className="text-left text-sm text-slate-300 font-mono overflow-x-auto">
{`// تعريف دالة في نيكسو
func add(a: Int, b: Int) -> Int {
    return a + b
}

// استدعاء الدالة
let result = add(10, 20)
print(result) // 30

// استخدام المكتبة القياسية
let pi = math_pi()
let area = pi * math_pow(5, 2)
print(area)`}
              </pre>
            </div>
          </div>
        </div>
      </section>

      {/* Editor Section */}
      <section id="editor" className="py-20 px-4 border-t border-slate-700/50">
        <div className="container">
          <h2 className="text-4xl font-bold text-white mb-8 text-center">جرب نيكسو الآن</h2>
          <p className="text-slate-300 text-center mb-12 max-w-2xl mx-auto">
            استخدم المحرر التفاعلي لكتابة واختبار كود نيكسو مباشرة في المتصفح
          </p>
          
          <Button 
            onClick={() => setLocation("/editor")}
            className="mx-auto block px-8 py-6 bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600 text-white text-lg rounded-lg"
          >
            <Code2 className="w-5 h-5 mr-2" />
            فتح المحرر
          </Button>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-slate-700/50 py-12 px-4">
        <div className="container text-center text-slate-400">
          <p>© 2026 Nexo Programming Language. جميع الحقوق محفوظة.</p>
          <p className="mt-2 text-sm">صُنعت بـ ❤️ لمستقبل البرمجة</p>
        </div>
      </footer>
    </div>
  );
}
