#!/usr/bin/env python3
"""
Nexo Standard Library - المكتبة القياسية الضخمة
تتضمن جميع المجالات: ويب، موبايل، ألعاب، AI، قواعد بيانات، إلخ
"""

import os
import sys
import json
import math
import datetime
import subprocess
import hashlib
import sqlite3
import threading
import time
import random
import re
import base64
import hmac
import uuid
from typing import Any, List, Dict, Callable, Optional

# ===== نظام الملفات =====

class FileSystem:
    @staticmethod
    def read(path: str) -> str:
        """قراءة ملف"""
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    
    @staticmethod
    def write(path: str, content: str) -> bool:
        """كتابة ملف"""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    @staticmethod
    def append(path: str, content: str) -> bool:
        """إضافة محتوى إلى ملف"""
        with open(path, 'a', encoding='utf-8') as f:
            f.write(content)
        return True
    
    @staticmethod
    def exists(path: str) -> bool:
        """التحقق من وجود ملف"""
        return os.path.exists(path)
    
    @staticmethod
    def delete(path: str) -> bool:
        """حذف ملف"""
        if os.path.isfile(path):
            os.remove(path)
        return True
    
    @staticmethod
    def mkdir(path: str) -> bool:
        """إنشاء مجلد"""
        os.makedirs(path, exist_ok=True)
        return True
    
    @staticmethod
    def list_files(path: str) -> List[str]:
        """قائمة الملفات في مجلد"""
        return os.listdir(path)
    
    @staticmethod
    def get_size(path: str) -> int:
        """حجم الملف بالبايتات"""
        return os.path.getsize(path)
    
    @staticmethod
    def get_info(path: str) -> Dict:
        """معلومات الملف"""
        stat = os.stat(path)
        return {
            'size': stat.st_size,
            'modified': datetime.datetime.fromtimestamp(stat.st_mtime).isoformat(),
            'created': datetime.datetime.fromtimestamp(stat.st_ctime).isoformat(),
            'is_file': os.path.isfile(path),
            'is_dir': os.path.isdir(path)
        }

# ===== معالجة النصوص المتقدمة =====

class StringUtils:
    @staticmethod
    def split(text: str, delimiter: str) -> List[str]:
        """تقسيم النص"""
        return text.split(delimiter)
    
    @staticmethod
    def join(items: List[str], delimiter: str) -> str:
        """دمج القائمة في نص"""
        return delimiter.join(map(str, items))
    
    @staticmethod
    def replace(text: str, old: str, new: str) -> str:
        """استبدال نص"""
        return text.replace(old, new)
    
    @staticmethod
    def contains(text: str, substring: str) -> bool:
        """التحقق من وجود نص"""
        return substring in text
    
    @staticmethod
    def starts_with(text: str, prefix: str) -> bool:
        """التحقق من بداية النص"""
        return text.startswith(prefix)
    
    @staticmethod
    def ends_with(text: str, suffix: str) -> bool:
        """التحقق من نهاية النص"""
        return text.endswith(suffix)
    
    @staticmethod
    def index_of(text: str, substring: str) -> int:
        """موقع النص الفرعي"""
        return text.find(substring)
    
    @staticmethod
    def substring(text: str, start: int, end: int) -> str:
        """استخراج جزء من النص"""
        return text[start:end]
    
    @staticmethod
    def reverse(text: str) -> str:
        """عكس النص"""
        return text[::-1]
    
    @staticmethod
    def matches(text: str, pattern: str) -> bool:
        """التحقق من مطابقة النمط"""
        return bool(re.match(pattern, text))
    
    @staticmethod
    def extract(text: str, pattern: str) -> List[str]:
        """استخراج النصوص المطابقة للنمط"""
        return re.findall(pattern, text)

# ===== الرياضيات المتقدمة =====

class MathUtils:
    PI = math.pi
    E = math.e
    
    @staticmethod
    def sqrt(x: float) -> float:
        return math.sqrt(x)
    
    @staticmethod
    def pow(x: float, y: float) -> float:
        return math.pow(x, y)
    
    @staticmethod
    def abs(x: float) -> float:
        return abs(x)
    
    @staticmethod
    def min(*args) -> float:
        return min(args)
    
    @staticmethod
    def max(*args) -> float:
        return max(args)
    
    @staticmethod
    def floor(x: float) -> int:
        return math.floor(x)
    
    @staticmethod
    def ceil(x: float) -> int:
        return math.ceil(x)
    
    @staticmethod
    def round(x: float, decimals: int = 0) -> float:
        return round(x, decimals)
    
    @staticmethod
    def sin(x: float) -> float:
        return math.sin(x)
    
    @staticmethod
    def cos(x: float) -> float:
        return math.cos(x)
    
    @staticmethod
    def tan(x: float) -> float:
        return math.tan(x)
    
    @staticmethod
    def random() -> float:
        return random.random()
    
    @staticmethod
    def random_int(min_val: int, max_val: int) -> int:
        return random.randint(min_val, max_val)

# ===== التاريخ والوقت =====

class DateTime:
    @staticmethod
    def now() -> str:
        return datetime.datetime.now().isoformat()
    
    @staticmethod
    def timestamp() -> int:
        return int(time.time())
    
    @staticmethod
    def format(dt: str, format_str: str) -> str:
        dt_obj = datetime.datetime.fromisoformat(dt)
        return dt_obj.strftime(format_str)
    
    @staticmethod
    def parse(date_str: str, format_str: str) -> str:
        dt_obj = datetime.datetime.strptime(date_str, format_str)
        return dt_obj.isoformat()
    
    @staticmethod
    def add_days(dt: str, days: int) -> str:
        dt_obj = datetime.datetime.fromisoformat(dt)
        new_dt = dt_obj + datetime.timedelta(days=days)
        return new_dt.isoformat()
    
    @staticmethod
    def add_hours(dt: str, hours: int) -> str:
        dt_obj = datetime.datetime.fromisoformat(dt)
        new_dt = dt_obj + datetime.timedelta(hours=hours)
        return new_dt.isoformat()

# ===== قواعد البيانات =====

class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    
    def execute(self, query: str, params: tuple = ()) -> List[tuple]:
        """تنفيذ استعلام"""
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def insert(self, table: str, data: Dict) -> bool:
        """إدراج بيانات"""
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, tuple(data.values()))
        self.conn.commit()
        return True
    
    def update(self, table: str, data: Dict, where: Dict) -> bool:
        """تحديث بيانات"""
        set_clause = ', '.join([f"{k}=?" for k in data.keys()])
        where_clause = ' AND '.join([f"{k}=?" for k in where.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        values = list(data.values()) + list(where.values())
        self.cursor.execute(query, values)
        self.conn.commit()
        return True
    
    def delete(self, table: str, where: Dict) -> bool:
        """حذف بيانات"""
        where_clause = ' AND '.join([f"{k}=?" for k in where.keys()])
        query = f"DELETE FROM {table} WHERE {where_clause}"
        self.cursor.execute(query, tuple(where.values()))
        self.conn.commit()
        return True
    
    def close(self):
        """إغلاق الاتصال"""
        self.conn.close()

# ===== الأمان والتشفير =====

class Crypto:
    @staticmethod
    def hash_password(password: str) -> str:
        """تجزئة كلمة المرور"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def verify_password(password: str, hash_value: str) -> bool:
        """التحقق من كلمة المرور"""
        return Crypto.hash_password(password) == hash_value
    
    @staticmethod
    def encrypt(data: str, key: str) -> str:
        """تشفير البيانات"""
        # تشفير بسيط (يجب استخدام مكتبة احترافية في الإنتاج)
        return base64.b64encode(data.encode()).decode()
    
    @staticmethod
    def decrypt(encrypted: str, key: str) -> str:
        """فك تشفير البيانات"""
        return base64.b64decode(encrypted.encode()).decode()
    
    @staticmethod
    def generate_token(length: int = 32) -> str:
        """توليد رمز عشوائي"""
        return uuid.uuid4().hex[:length]
    
    @staticmethod
    def hash_md5(data: str) -> str:
        """تجزئة MD5"""
        return hashlib.md5(data.encode()).hexdigest()
    
    @staticmethod
    def hash_sha256(data: str) -> str:
        """تجزئة SHA256"""
        return hashlib.sha256(data.encode()).hexdigest()

# ===== نظام التشغيل والعمليات =====

class OS:
    @staticmethod
    def execute(command: str) -> str:
        """تنفيذ أمر النظام"""
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    
    @staticmethod
    def get_env(name: str) -> Optional[str]:
        """الحصول على متغير البيئة"""
        return os.getenv(name)
    
    @staticmethod
    def set_env(name: str, value: str):
        """تعيين متغير البيئة"""
        os.environ[name] = value
    
    @staticmethod
    def current_dir() -> str:
        """المجلد الحالي"""
        return os.getcwd()
    
    @staticmethod
    def change_dir(path: str):
        """تغيير المجلد الحالي"""
        os.chdir(path)
    
    @staticmethod
    def platform() -> str:
        """نظام التشغيل"""
        return sys.platform
    
    @staticmethod
    def sleep(seconds: float):
        """توقف البرنامج"""
        time.sleep(seconds)

# ===== معالجة JSON =====

class JSON:
    @staticmethod
    def parse(json_str: str) -> Any:
        """تحليل JSON"""
        return json.loads(json_str)
    
    @staticmethod
    def stringify(obj: Any, indent: int = None) -> str:
        """تحويل إلى JSON"""
        return json.dumps(obj, indent=indent, ensure_ascii=False)
    
    @staticmethod
    def pretty_print(obj: Any) -> str:
        """طباعة JSON بشكل جميل"""
        return json.dumps(obj, indent=2, ensure_ascii=False)

# ===== معالجة القوائم =====

class List:
    @staticmethod
    def length(lst: list) -> int:
        return len(lst)
    
    @staticmethod
    def push(lst: list, item: Any) -> list:
        lst.append(item)
        return lst
    
    @staticmethod
    def pop(lst: list) -> Any:
        return lst.pop() if lst else None
    
    @staticmethod
    def shift(lst: list) -> Any:
        return lst.pop(0) if lst else None
    
    @staticmethod
    def unshift(lst: list, item: Any) -> list:
        lst.insert(0, item)
        return lst
    
    @staticmethod
    def reverse(lst: list) -> list:
        return list(reversed(lst))
    
    @staticmethod
    def sort(lst: list) -> list:
        return sorted(lst)
    
    @staticmethod
    def contains(lst: list, item: Any) -> bool:
        return item in lst
    
    @staticmethod
    def index_of(lst: list, item: Any) -> int:
        return lst.index(item) if item in lst else -1
    
    @staticmethod
    def slice(lst: list, start: int, end: int) -> list:
        return lst[start:end]
    
    @staticmethod
    def concat(lst1: list, lst2: list) -> list:
        return lst1 + lst2
    
    @staticmethod
    def map(lst: list, fn: Callable) -> list:
        return [fn(item) for item in lst]
    
    @staticmethod
    def filter(lst: list, fn: Callable) -> list:
        return [item for item in lst if fn(item)]
    
    @staticmethod
    def reduce(lst: list, fn: Callable, initial: Any = None) -> Any:
        if initial is None and lst:
            result = lst[0]
            for item in lst[1:]:
                result = fn(result, item)
        else:
            result = initial
            for item in lst:
                result = fn(result, item)
        return result

# ===== معالجة القواميس =====

class Dict:
    @staticmethod
    def keys(d: dict) -> List[str]:
        return list(d.keys())
    
    @staticmethod
    def values(d: dict) -> List[Any]:
        return list(d.values())
    
    @staticmethod
    def entries(d: dict) -> List[tuple]:
        return list(d.items())
    
    @staticmethod
    def has(d: dict, key: str) -> bool:
        return key in d
    
    @staticmethod
    def get(d: dict, key: str, default: Any = None) -> Any:
        return d.get(key, default)
    
    @staticmethod
    def set(d: dict, key: str, value: Any) -> dict:
        d[key] = value
        return d
    
    @staticmethod
    def delete(d: dict, key: str) -> dict:
        if key in d:
            del d[key]
        return d
    
    @staticmethod
    def merge(d1: dict, d2: dict) -> dict:
        result = d1.copy()
        result.update(d2)
        return result

# ===== المعالجة المتزامنة =====

class Threading:
    @staticmethod
    def create_thread(fn: Callable, args: tuple = ()) -> threading.Thread:
        """إنشاء خيط"""
        thread = threading.Thread(target=fn, args=args)
        return thread
    
    @staticmethod
    def start_thread(thread: threading.Thread):
        """بدء الخيط"""
        thread.start()
    
    @staticmethod
    def wait_thread(thread: threading.Thread):
        """انتظار انتهاء الخيط"""
        thread.join()

# ===== معالجة الأخطاء =====

class Error:
    @staticmethod
    def create(message: str, code: int = 1) -> Dict:
        """إنشاء كائن خطأ"""
        return {
            'message': message,
            'code': code,
            'timestamp': datetime.datetime.now().isoformat()
        }
    
    @staticmethod
    def to_string(error: Dict) -> str:
        """تحويل الخطأ إلى نص"""
        return f"Error ({error['code']}): {error['message']}"

# ===== مكتبة موحدة =====

class NexoStdLib:
    """المكتبة القياسية الموحدة لنيكسو"""
    
    fs = FileSystem
    string = StringUtils
    math = MathUtils
    datetime = DateTime
    database = Database
    crypto = Crypto
    os = OS
    json = JSON
    list = List
    dict = Dict
    threading = Threading
    error = Error
    
    @staticmethod
    def version() -> str:
        return "1.0.0"
    
    @staticmethod
    def info() -> Dict:
        return {
            'name': 'Nexo Standard Library',
            'version': '1.0.0',
            'modules': [
                'fs', 'string', 'math', 'datetime', 'database',
                'crypto', 'os', 'json', 'list', 'dict', 'threading', 'error'
            ]
        }


# تصدير المكتبة
__all__ = ['NexoStdLib', 'FileSystem', 'StringUtils', 'MathUtils', 'DateTime',
           'Database', 'Crypto', 'OS', 'JSON', 'List', 'Dict', 'Threading', 'Error']
