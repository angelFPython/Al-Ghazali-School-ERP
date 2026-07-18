-- جدول إعدادات المدرسة (لإدارة بيانات مدرسة الغزالي)
CREATE TABLE school_settings (
    id SERIAL PRIMARY KEY,
    school_name VARCHAR(255) DEFAULT 'مدرسة الغزالي',
    director_name VARCHAR(255),
    deputy_name VARCHAR(255),
    logo_path VARCHAR(255),
    stamp_path VARCHAR(255),
    governorate VARCHAR(100) DEFAULT 'اليمن',
    district VARCHAR(100),
    phone_numbers TEXT,
    email VARCHAR(100),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- إدراج البيانات الافتراضية للمدرسة
INSERT INTO school_settings (school_name, governorate) 
VALUES ('مدرسة الغزالي', 'اليمن');

