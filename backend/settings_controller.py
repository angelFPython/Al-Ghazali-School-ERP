from flask import Flask, request, jsonify

app = Flask(__name__)

# محاكاة لقاعدة بيانات المعلمين
teachers_db = {}

# 1. إضافة معلم جديد
@app.route('/api/teachers/add', methods=['POST'])
def add_teacher():
    data = request.json
    emp_id = data.get('employee_number')
    teachers_db[emp_id] = data
    return jsonify({"status": "success", "message": f"تم إضافة المعلم {data.get('full_name')} بنجاح"})

# 2. جلب جميع المعلمين
@app.route('/api/teachers/list', methods=['GET'])
def list_teachers():
    return jsonify(list(teachers_db.values()))

# 3. إرسال إشعار للمعلم (واتساب / إشعار نظام)
@app.route('/api/teachers/send-notification', methods=['POST'])
def send_notification():
    data = request.json
    teacher_id = data.get('teacher_id')
    message = data.get('message')
    method = data.get('method') # 'whatsapp', 'sms', 'system'
    
    # هنا يتم الربط البرمجي الفعلي مع بوابة الواتساب
    # مثال: if method == 'whatsapp': send_whatsapp_api(teacher_phone, message)
    
    print(f"إرسال عبر {method} إلى المعلم {teacher_id}: {message}")
    
    return jsonify({
        "status": "success", 
        "message": f"تم إرسال الإشعار بنجاح عبر {method}"
    })

# (تذكير: دمجنا هنا دالة get_menu من الكود السابق للحفاظ على تكامل النظام)
@app.route('/api/get-menu', methods=['GET'])
def get_menu():
    # ... نفس كود الصلاحيات السابق ...
    return jsonify({"menu": ["إدارة المعلمين", "إرسال إشعار"]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
