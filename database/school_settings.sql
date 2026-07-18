-- 1. جدول إعدادات المدرسة (لإدارة بيانات مدرسة الغزالي)
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

-- 2. إدراج البيانات الافتراضية للمدرسة
INSERT INTO school_settings (school_name, governorate) 
VALUES ('مدرسة الغزالي', 'اليمن');

-- 3. جدول المستخدمين والصلاحيات
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    role VARCHAR(50) NOT NULL, -- (admin, control, teacher, accountant, student, parent)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. إدراج حساب المدير الافتراضي (كلمة السر يجب تشفيرها لاحقاً)
INSERT INTO users (username, password_hash, full_name, role) 
VALUES ('admin', 'hashed_password_here', 'مدير النظام', 'admin');
