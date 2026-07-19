-- الجداول الأساسية
CREATE TABLE school_settings (id SERIAL PRIMARY KEY, school_name TEXT, director_name TEXT, logo_path TEXT, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password_hash TEXT, role TEXT);
CREATE TABLE teachers (id SERIAL PRIMARY KEY, full_name TEXT, employee_number TEXT UNIQUE, phone TEXT, whatsapp TEXT, specialization TEXT, photo_path TEXT);
CREATE TABLE students (id SERIAL PRIMARY KEY, full_name TEXT, seat_number TEXT UNIQUE, school_id TEXT UNIQUE, class_level TEXT, parent_whatsapp TEXT, photo_path TEXT);
CREATE TABLE finance (id SERIAL PRIMARY KEY, type TEXT, amount DECIMAL, description TEXT, student_id TEXT);
CREATE TABLE inventory (id SERIAL PRIMARY KEY, item_name TEXT, quantity INTEGER, category TEXT);
CREATE TABLE library (id SERIAL PRIMARY KEY, book_title TEXT, author TEXT, status TEXT);
CREATE TABLE transport (id SERIAL PRIMARY KEY, bus_number TEXT, driver_name TEXT, route TEXT);
CREATE TABLE health_records (id SERIAL PRIMARY KEY, student_id TEXT, diagnosis TEXT, treatment TEXT);
CREATE TABLE official_docs (id SERIAL PRIMARY KEY, doc_type TEXT, serial_number TEXT UNIQUE, content TEXT);

-- إدراج بيانات افتتاحية
INSERT INTO school_settings (school_name) VALUES ('مدرسة الغزالي');
