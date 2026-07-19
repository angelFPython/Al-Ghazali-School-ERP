from flask import Flask, request, jsonify
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)

# إعداد قاعدة البيانات (يتم الإنشاء تلقائياً في أول تشغيل)
DB_NAME = "database/school_data.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# --- وحدة الطلاب ---
@app.route('/api/students/add', methods=['POST'])
def add_student():
    data = request.json
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (full_name, seat_number, school_id, parent_whatsapp) VALUES (?, ?, ?, ?)",
                   (data['name'], data['seat_number'], data['school_id'], data['parent_whatsapp']))
    conn.commit()
    return jsonify({"status": "success", "message": "تم إضافة الطالب بنجاح"})

# --- وحدة المعلمين ---
@app.route('/api/teachers/add', methods=['POST'])
def add_teacher():
    data = request.json
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO teachers (full_name, emp_number, phone, whatsapp, specialization) VALUES (?, ?, ?, ?, ?)",
                   (data['name'], data['emp_number'], data['phone'], data['whatsapp'], data['specialization']))
    conn.commit()
    return jsonify({"status": "success", "message": "تم إضافة المعلم بنجاح"})

# --- وحدة الإشعارات (واتساب / SMS / بريد) ---
@app.route('/api/notifications/send', methods=['POST'])
def send_notification():
    data = request.json
    # هذا المكان يتم فيه الربط مع بوابة واتساب API أو SMS Gateway
    method = data.get('method') # 'whatsapp', 'sms', 'email'
    recipient = data.get('recipient')
    message = data.get('message')
    
    print(f"إرسال عبر {method} إلى {recipient}: {message}")
    return jsonify({"status": "success", "message": "تم إرسال الإشعار بنجاح"})

# --- وحدة النماذج الرسمية (الجمهورية اليمنية) ---
@app.route('/api/docs/generate', methods=['POST'])
def generate_official_doc():
    data = request.json
    # هنا يتم إنشاء الوثيقة بتنسيق الجمهورية اليمنية
    doc_content = f"""
    الجمهورية اليمنية
    وزارة التربية والتعليم
    مدرسة الغزالي
    ---
    الموضوع: {data['subject']}
    إلى: {data['recipient']}
    {data['body']}
    ---
    التوقيع والختم: [ختم المدرسة]
    """
    return jsonify({"status": "success", "doc_content": doc_content})

# --- وحدة الذكاء الاصطناعي ---
@app.route('/api/ai/analyze', methods=['POST'])
def ai_analyze():
    data = request.json
    # تحليل بيانات الطالب وتوقع مستواه
    # هذا الكود هو نقطة الانطلاق لمنطق الـ AI
    analysis = "النتيجة: الطالب متفوق ويحتاج تشجيع، نسبة التسرب: 0%"
    return jsonify({"status": "success", "analysis": analysis})

# --- وحدة الصلاحيات (التحكم في القوائم) ---
@app.route('/api/auth/menu', methods=['GET'])
def get_menu():
    role = request.args.get('role', 'student')
    menus = {
        "admin": ["الكل", "إعدادات المدرسة", "المالية", "إدارة المعلمين"],
        "teacher": ["طلابي", "الحضور", "الرسائل"],
        "student": ["نتائجي", "جدولي"]
    }
    return jsonify({"menu": menus.get(role, [])})

if __name__ == '__main__':
    # التأكد من وجود مجلد قاعدة البيانات
    if not os.path.exists('database'):
        os.makedirs('database')
    app.run(debug=True)
