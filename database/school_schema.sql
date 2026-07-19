-- هيكل قاعدة بيانات نظام "مدرسة الغزالي" الذكي (Yemen Smart School ERP)

-- 1. الإعدادات العامة
CREATE TABLE IF NOT EXISTS school_settings (
    id SERIAL PRIMARY KEY,
    school_name TEXT DEFAULT 'مدرسة الغزالي',
    director_name TEXT,
    deputy_name TEXT,
    logo_path TEXT,
    stamp_path TEXT,
    governorate TEXT DEFAULT 'اليمن',
    district TEXT,
    phone_numbers TEXT,
    email TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. نظام المستخدمين والصلاحيات
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    full_name TEXT,
    role TEXT NOT NULL, -- (admin, control, teacher, accountant, student, parent)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. إدارة الكوادر التعليمية (المعلمون)
CREATE TABLE IF NOT EXISTS teachers (
    id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    emp_number TEXT UNIQUE NOT NULL,
    phone TEXT,
    whatsapp TEXT,
    specialization TEXT,
    subject TEXT,
    photo_path TEXT,
    tasks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. إدارة الطلاب (مع بيانات أولياء الأمور والصور)
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    seat_number TEXT UNIQUE,
    school_id TEXT UNIQUE NOT NULL,
    class_level TEXT,
    parent_whatsapp TEXT,
    photo_path TEXT,
    status TEXT DEFAULT 'active', -- (active, withdrawn, graduated)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 5. الإدارة المالية والمخازن
CREATE TABLE IF NOT EXISTS finance (
    id SERIAL PRIMARY KEY,
    type TEXT, -- (income, expense)
    amount DECIMAL(15,2),
    description TEXT,
    student_id TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. الأرشيف الرسمي للنماذج (بشعار الجمهورية)
CREATE TABLE IF NOT EXISTS official_docs (
    id SERIAL PRIMARY KEY,
    doc_type TEXT,
    recipient_name TEXT,
    content TEXT,
    serial_number TEXT UNIQUE,
    created_by TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- إدراج البيانات الأساسية الافتراضية
INSERT INTO school_settings (school_name) VALUES ('مدرسة الغزالي');
INSERT INTO users (username, password_hash, full_name, role) VALUES ('admin', 'hashed_admin_pass', 'مدير النظام', 'admin');
