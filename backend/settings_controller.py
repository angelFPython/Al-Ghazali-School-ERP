# كود مبدئي للتعامل مع إعدادات المدرسة
from flask import Flask, request, jsonify

app = Flask(__name__)

# وظيفة لتحديث اسم المدرسة أو بياناتها
@app.route('/api/update-school-info', methods=['POST'])
def update_school_info():
    data = request.json
    # هنا سيتم ربط الكود بقاعدة البيانات التي أنشأناها
    # تحديث اسم المدرسة، الشعار، المدير.. إلخ
    print(f"تم تحديث بيانات المدرسة إلى: {data['school_name']}")
    return jsonify({"status": "success", "message": "تم حفظ بيانات مدرسة الغزالي بنجاح"})

if __name__ == '__main__':
    app.run(debug=True)

