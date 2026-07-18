from flask import Flask, request, jsonify

app = Flask(__name__)

# محاكاة لقاعدة بيانات المستخدمين (لغرض التطوير)
users_db = {
    "admin": {"role": "admin", "full_name": "مدير النظام"},
    "teacher1": {"role": "teacher", "full_name": "أستاذ المادة"},
    "control": {"role": "control", "full_name": "موظف الكنترول"}
}

# 1. إرجاع بيانات المدرسة (إعدادات مدرسة الغزالي)
@app.route('/api/school-settings', methods=['GET'])
def get_settings():
    # هنا سيتم استرجاع البيانات الحقيقية من جدول school_settings
    return jsonify({
        "school_name": "مدرسة الغزالي",
        "governorate": "اليمن",
        "director": "مدير المدرسة"
    })

# 2. نظام القوائم الديناميكي بناءً على الصلاحيات
@app.route('/api/get-menu', methods=['GET'])
def get_menu():
    username = request.args.get('username')
    user = users_db.get(username)
    
    if not user:
        return jsonify({"error": "مستخدم غير موجود"}), 404
        
    # تعريف القوائم لكل صلاحية
    roles_menu = {
        "admin": ["إعدادات المدرسة", "إدارة المعلمين", "إدارة الطلاب", "المالية", "التقارير", "صلاحيات المستخدمين"],
        "teacher": ["طلابي", "إرسال إشعار", "جدول الحصص", "رصد الدرجات"],
        "control": ["إدارة الاختبارات", "رصد الدرجات", "الشهادات", "التقارير"]
    }
    
    menu = roles_menu.get(user['role'], [])
    return jsonify({"role": user['role'], "menu": menu})

# 3. تحديث بيانات المدرسة
@app.route('/api/update-school-info', methods=['POST'])
def update_school_info():
    data = request.json
    # هنا يتم الربط مع قاعدة البيانات لتحديث البيانات
    return jsonify({"status": "success", "message": f"تم تحديث بيانات {data.get('school_name')} بنجاح"})

if __name__ == '__main__':
    # تشغيل التطبيق
    app.run(debug=True, port=5000)
