from flask import Flask, request, jsonify

app = Flask(__name__)

# قاعدة بيانات مالية مؤقتة
financial_records = []

# 1. تسجيل عملية مالية (قبض رسوم أو مصروفات)
@app.route('/api/finance/add-transaction', methods=['POST'])
def add_transaction():
    data = request.json
    # data مثال: {"type": "income", "amount": 5000, "description": "رسوم دراسية", "student_id": "123"}
    financial_records.append(data)
    return jsonify({"status": "success", "message": "تم تسجيل العملية المالية بنجاح"})

# 2. استخراج كشف حساب (إيرادات ومصروفات)
@app.route('/api/finance/report', methods=['GET'])
def get_finance_report():
    total_income = sum(item['amount'] for item in financial_records if item['type'] == 'income')
    total_expense = sum(item['amount'] for item in financial_records if item['type'] == 'expense')
    
    return jsonify({
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense,
        "details": financial_records
    })

# 3. طباعة سند قبض/صرف (تصدير بيانات)
@app.route('/api/finance/print-receipt/<transaction_id>', methods=['GET'])
def print_receipt(transaction_id):
    # هنا سنربط لاحقاً بمكتبة PDF لإنشاء سند رسمي بالختم
    return jsonify({"status": "success", "message": "جاري إنشاء السند للطباعة"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)

