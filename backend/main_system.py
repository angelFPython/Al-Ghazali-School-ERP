import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# إعدادات المجلدات للصور والوثائق
UPLOAD_FOLDER = 'uploads/students/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# قاعدة بيانات محاكاة شاملة
db = {
    "users": {"admin": {"role": "admin", "full_name": "مدير النظام"}},
    "teachers": {},
    "students": {},
    "finance": [],
    "docs": [],
    "ai_analysis": {}
}

# --- 1. إعدادات المدرسة والصلاحيات ---
@app.route('/api/school-settings', methods=['GET'])
def get_settings():
    return jsonify({"school_name": "مدرسة الغزالي", "governorate": "اليمن"})

@app.route('/api/get-menu', methods=['GET'])
def get_menu():
    username = request.args.get('username')
    user = db["users"].get(username, {"role": "guest"})
    roles_menu = {
        "admin": ["إعدادات المدرسة", "إدارة المعلمين", "إدارة الطلاب", "المالية", "التقارير", "الوثائق الرسمية", "المساعد الذكي"],
        "teacher": ["طلابي", "إرسال إشعار", "جدول الحصص"],
        "control": ["إدارة الاختبارات", "رصد الدرجات", "الشهادات"]
    }
    return jsonify({"menu": roles_menu.get(user['role'], [])})

# --- 2. إدارة المعلمين ---
@app.route('/api/teachers/add', methods=['POST'])
def add_teacher():
    data = request.json
    db["teachers"][data['employee_number']] = data
    return jsonify({"status": "success", "message": "تم إضافة المعلم بنجاح"})

# --- 3. إدارة الطلاب مع رفع الصور ---
@app.route('/api/students/add', methods=['POST'])
def add_student():
    data = request.form
    student_id = data.get('school_id')
    photo_path = None
    if 'photo' in request.files:
        photo = request.files['photo']
        filename = secure_filename(f"{student_id}_{photo.filename}")
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        photo_path = os.path.join(UPLOAD_FOLDER, filename)
    db["students"][student_id] = {**data, "photo_path": photo_path}
    return jsonify({"status": "success", "message": "تم إضافة الطالب بنجاح"})

# --- 4. الإدارة المالية ---
@app.route('/api/finance/add', methods=['POST'])
def add_finance():
    db["finance"].append(request.json)
    return jsonify({"status": "success", "message": "تم تسجيل العملية المالية"})

# --- 5. الوثائق الرسمية ---
@app.route('/api/docs/generate', methods=['POST'])
def generate_doc():
    doc_data = request.json
    db["docs"].append(doc_data)
    return jsonify({"status": "success", "message": "تم إصدار الوثيقة رسمياً"})

# --- 6. وحدة الذكاء الاصطناعي ---
@app.route('/api/ai/predict-performance', methods=['POST'])
def predict_performance():
    data = request.json
    grades = data.get('grades', [])
    avg = sum(grades) / len(grades) if grades else 0
    risk = "مرتفع" if avg < 50 else "منخفض"
    return jsonify({"risk_level": risk, "suggestion": "يُنصح بعمل دروس تقوية" if risk == "مرتفع" else "مستوى الطالب ممتاز"})

@app.route('/api/ai/chat-assistant', methods=['POST'])
def chat_assistant():
    query = request.json.get('query', '')
    return jsonify({"answer": f"المساعد الذكي لمدرسة الغزالي يحلل طلبك: {query}"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
