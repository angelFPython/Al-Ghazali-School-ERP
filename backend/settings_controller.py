from flask import Flask, request, jsonify

app = Flask(__name__)

# محاكاة لقاعدة بيانات المستخدمين
users = {
    "admin": {"role": "admin", "permissions": ["all"]},
    "teacher1": {"role": "teacher", "permissions": ["view_students", "send_notifications"]}
}

@app.route('/api/get-menu', methods=['GET'])
def get_menu():
    username = request.args.get('username')
    user = users.get(username)
    
    if not user:
        return jsonify({"error": "مستخدم غير موجود"}), 404
        
    # هنا يتم إرجاع القائمة بناءً على الصلاحية
    if user['role'] == 'admin':
        return jsonify({"menu": ["إعدادات المدرسة", "إدارة المعلمين", "إدارة الطلاب", "المالية", "التقارير"]})
    elif user['role'] == 'teacher':
        return jsonify({"menu": ["طلابي", "إرسال إشعار", "جدول الحصص"]})
    
    return jsonify({"menu": []})

if __name__ == '__main__':
    app.run(debug=True)
