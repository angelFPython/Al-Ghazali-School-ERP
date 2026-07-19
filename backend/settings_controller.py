import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# إعدادات المجلدات
UPLOAD_FOLDER = 'uploads/students/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# قاعدة بيانات مؤقتة (سيتم ربطها لاحقاً بـ PostgreSQL)
users_db = {"admin": {"role": "admin"}, "teacher1": {"role": "teacher"}}
teachers_db = {}
students_db = {}

# --- إدارة الإعدادات ---
@app.route('/api/school-settings', methods=['GET'])
def get_settings():
    return jsonify({"school_name": "مدرسة الغزالي", "governorate": "اليمن"})

# --- نظام القوائم والصلاحيات ---
@app.route('/api/get-menu', methods=['GET'])
def get_menu():
    username = request.args.get('username')
    user = users_db.get(username, {"role": "guest"})
    roles_menu = {
        "admin": ["إعدادات المدرسة", "إدارة المعلمين", "إدارة الطلاب", "المالية", "التقارير"],
        "teacher": ["طلابي", "إرسال إشعار", "جدول الحصص"]
    }
    return jsonify({"menu": roles_menu.get(user['role'], [])})

# --- إدارة المعلمين ---
@app.route('/api/teachers/add', methods=['POST'])
def add_teacher():
    data = request.json
    teachers_db[data['employee_number']] = data
    return jsonify({"status": "success", "message": "تم إضافة المعلم"})

@app.route('/api/teachers/send-notification', methods=['POST'])
def send_notification():
    data = request.json
    # ربط برمجية الـ WhatsApp API هنا
    return jsonify({"status": "success", "message": "تم الإرسال عبر " + data.get('method')})

# --- إدارة الطلاب مع رفع الصور ---
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
    
    students_db[student_id] = {**data, "photo_path": photo_path}
    return jsonify({"status": "success", "message": "تم إضافة الطالب بنجاح"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
