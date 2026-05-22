import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Play, Copy, RotateCcw, ArrowLeft } from "lucide-react";
import { useState } from "react";
import { useLocation } from "wouter";
import { toast } from "sonner";

const EXAMPLES = {
  hello: `let greeting = "مرحباً بك في نيكسو!"
print(greeting)`,
  
  math: `let x = 10
let y = 20
let sum = x + y
let product = x * y
print("المجموع: " + str(sum))
print("الضرب: " + str(product))`,
  
  advanced: `let name = "نيكسو"
let version = 1.0
print("لغة " + name)
print("الإصدار: " + str(version))

let radius = 5
let pi = math_pi()
let area = pi * math_pow(radius, 2)
print("مساحة الدائرة: " + str(area))

let time = time_now()
print("الوقت الحالي: " + time)`
};

export default function Editor() {
  const [, setLocation] = useLocation();
  const [code, setCode] = useState(EXAMPLES.hello);
  const [output, setOutput] = useState("");
  const [isRunning, setIsRunning] = useState(false);

  const runCode = async () => {
    setIsRunning(true);
    setOutput("جاري التنفيذ...\n");
    
    try {
      // محاكاة تنفيذ الكود
      const lines = code.split('\n');
      let result = "";
      let variables: Record<string, any> = {};

      for (const line of lines) {
        const trimmed = line.trim();
        if (!trimmed || trimmed.startsWith('//')) continue;

        // معالجة let
        const letMatch = trimmed.match(/let\s+(\w+)\s*=\s*(.*)/);
        if (letMatch) {
          const [, varName, expr] = letMatch;
          variables[varName] = evaluateExpression(expr, variables);
          continue;
        }

        // معالجة print
        const printMatch = trimmed.match(/print\((.*)\)/);
        if (printMatch) {
          const [, expr] = printMatch;
          const value = evaluateExpression(expr, variables);
          result += String(value) + "\n";
          continue;
        }
      }

      setOutput(result || "لا يوجد مخرجات");
      toast.success("تم تنفيذ الكود بنجاح!");
    } catch (error) {
      setOutput(`خطأ: ${error instanceof Error ? error.message : 'خطأ غير معروف'}`);
      toast.error("حدث خطأ أثناء التنفيذ");
    } finally {
      setIsRunning(false);
    }
  };

  const evaluateExpression = (expr: string, vars: Record<string, any>): any => {
    expr = expr.trim();

    // Strings
    if ((expr.startsWith('"') && expr.endsWith('"')) || (expr.startsWith("'") && expr.endsWith("'"))) {
      return expr.slice(1, -1);
    }

    // Numbers
    if (!isNaN(Number(expr))) {
      return Number(expr);
    }

    // Variables
    if (expr in vars) {
      return vars[expr];
    }

    // Functions
    if (expr.includes('math_pi()')) {
      return Math.PI;
    }
    if (expr.includes('math_pow')) {
      const match = expr.match(/math_pow\((\d+),\s*(\d+)\)/);
      if (match) return Math.pow(Number(match[1]), Number(match[2]));
    }
    if (expr.includes('math_sqrt')) {
      const match = expr.match(/math_sqrt\((\d+)\)/);
      if (match) return Math.sqrt(Number(match[1]));
    }
    if (expr.includes('time_now()')) {
      return new Date().toLocaleString('ar-SA');
    }
    if (expr.includes('str(')) {
      const match = expr.match(/str\((.*)\)/);
      if (match) return String(evaluateExpression(match[1], vars));
    }

    // Arithmetic
    if (expr.includes('+')) {
      const parts = expr.split('+');
      return evaluateExpression(parts[0], vars) + evaluateExpression(parts[1], vars);
    }
    if (expr.includes('-') && !expr.startsWith('-')) {
      const parts = expr.split('-');
      return evaluateExpression(parts[0], vars) - evaluateExpression(parts[1], vars);
    }
    if (expr.includes('*')) {
      const parts = expr.split('*');
      return evaluateExpression(parts[0], vars) * evaluateExpression(parts[1], vars);
    }
    if (expr.includes('/')) {
      const parts = expr.split('/');
      return evaluateExpression(parts[0], vars) / evaluateExpression(parts[1], vars);
    }

    return expr;
  };

  const copyCode = () => {
    navigator.clipboard.writeText(code);
    toast.success("تم نسخ الكود!");
  };

  const resetCode = () => {
    setCode(EXAMPLES.hello);
    setOutput("");
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      {/* Header */}
      <div className="border-b border-slate-700/50 bg-slate-900/80 backdrop-blur-md sticky top-0 z-40">
        <div className="container py-4 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <Button 
              onClick={() => setLocation("/")}
              variant="ghost"
              className="text-slate-300 hover:text-white"
            >
              <ArrowLeft className="w-5 h-5 mr-2" />
              العودة
            </Button>
            <h1 className="text-2xl font-bold text-white">محرر نيكسو التفاعلي</h1>
          </div>
        </div>
      </div>

      <div className="container py-8">
        <div className="grid lg:grid-cols-2 gap-8">
          {/* Code Editor */}
          <div>
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-bold text-white">الكود</h2>
              <div className="flex gap-2">
                <Button 
                  onClick={copyCode}
                  variant="outline"
                  size="sm"
                  className="border-slate-600 text-slate-300 hover:bg-slate-800"
                >
                  <Copy className="w-4 h-4" />
                </Button>
                <Button 
                  onClick={resetCode}
                  variant="outline"
                  size="sm"
                  className="border-slate-600 text-slate-300 hover:bg-slate-800"
                >
                  <RotateCcw className="w-4 h-4" />
                </Button>
              </div>
            </div>

            <Card className="bg-slate-800/50 border-slate-700/50 p-4 mb-4">
              <Textarea 
                value={code}
                onChange={(e) => setCode(e.target.value)}
                className="bg-slate-900 border-slate-700 text-slate-100 font-mono text-sm min-h-96 resize-none"
                placeholder="اكتب كود نيكسو هنا..."
              />
            </Card>

            {/* Examples */}
            <div className="space-y-2">
              <p className="text-sm text-slate-400">أمثلة:</p>
              <div className="flex gap-2 flex-wrap">
                <Button 
                  onClick={() => setCode(EXAMPLES.hello)}
                  variant="outline"
                  size="sm"
                  className="border-slate-600 text-slate-300 hover:bg-slate-800"
                >
                  مرحباً
                </Button>
                <Button 
                  onClick={() => setCode(EXAMPLES.math)}
                  variant="outline"
                  size="sm"
                  className="border-slate-600 text-slate-300 hover:bg-slate-800"
                >
                  رياضيات
                </Button>
                <Button 
                  onClick={() => setCode(EXAMPLES.advanced)}
                  variant="outline"
                  size="sm"
                  className="border-slate-600 text-slate-300 hover:bg-slate-800"
                >
                  متقدم
                </Button>
              </div>
            </div>
          </div>

          {/* Output */}
          <div>
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-bold text-white">المخرجات</h2>
            </div>

            <Card className="bg-slate-800/50 border-slate-700/50 p-4 mb-4">
              <div className="bg-slate-900 rounded p-4 min-h-96 font-mono text-sm text-slate-100 whitespace-pre-wrap break-words">
                {output || "سيظهر الناتج هنا..."}
              </div>
            </Card>

            <Button 
              onClick={runCode}
              disabled={isRunning}
              className="w-full px-8 py-6 bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600 text-white text-lg rounded-lg"
            >
              <Play className="w-5 h-5 mr-2" />
              {isRunning ? "جاري التنفيذ..." : "تنفيذ الكود"}
            </Button>

            {/* Documentation */}
            <div className="mt-8 bg-slate-800/50 border border-slate-700/50 rounded-lg p-6">
              <h3 className="text-lg font-bold text-white mb-4">دليل سريع</h3>
              <div className="space-y-3 text-sm text-slate-300">
                <div>
                  <p className="font-mono text-cyan-400">let x = 10</p>
                  <p>تعريف متغير</p>
                </div>
                <div>
                  <p className="font-mono text-cyan-400">print("Hello")</p>
                  <p>طباعة نص</p>
                </div>
                <div>
                  <p className="font-mono text-cyan-400">math_pi(), math_pow(x, y)</p>
                  <p>دوال رياضية</p>
                </div>
                <div>
                  <p className="font-mono text-cyan-400">str(x), time_now()</p>
                  <p>دوال مساعدة</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
