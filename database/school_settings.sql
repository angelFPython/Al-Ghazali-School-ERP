-- 1. جدول إعدادات المدرسة
CREATE TABLE IF NOT EXISTS school_settings (
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

-- 2. جدول المستخدمين والصلاحيات
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    role VARCHAR(50) NOT NULL -- admin, control, teacher, accountant, student, parent
);

-- 3. جدول المعلمين
CREATE TABLE IF NOT EXISTS teachers (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    employee_number VARCHAR(50) UNIQUE NOT NULL,
    phone VARCHAR(20),
    whatsapp_number VARCHAR(20),
    specialization VARCHAR(100),
    subject VARCHAR(100),
    photo_path VARCHAR(255),
    tasks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. جدول الطلاب
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    seat_number VARCHAR(20) UNIQUE,
    school_id VARCHAR(50) UNIQUE NOT NULL,
    class_level VARCHAR(50),
    section VARCHAR(20),
    gender VARCHAR(10),
    birth_date DATE,
    address TEXT,
    parent_name VARCHAR(255),
    parent_whatsapp VARCHAR(20),
    photo_path VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 5. جدول العمليات المالية
CREATE TABLE IF NOT EXISTS finance (
    id SERIAL PRIMARY KEY,
    transaction_type VARCHAR(20), 
    amount DECIMAL(15, 2),
    description TEXT,
    category VARCHAR(50),
    student_id VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. جدول الأرشيف الرسمي للوثائق
CREATE TABLE IF NOT EXISTS official_docs (
    id SERIAL PRIMARY KEY,
    doc_type VARCHAR(100),
    recipient_name VARCHAR(255),
    issue_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    serial_number VARCHAR(50) UNIQUE,
    content TEXT,
    created_by VARCHAR(50)
);

-- البيانات الافتراضية
INSERT INTO school_settings (school_name, governorate) VALUES ('مدرسة الغزالي', 'اليمن');
INSERT INTO users (username, password_hash, full_name, role) VALUES ('admin', 'admin_hash_here', 'مدير النظام', 'admin');
