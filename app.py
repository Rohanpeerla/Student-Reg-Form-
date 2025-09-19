from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# ---------- DATABASE SETUP ----------
def init_db():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT,
            gender TEXT,
            dob TEXT,
            nationality TEXT,
            aadhar TEXT,
            email TEXT,
            phone TEXT,

            address1 TEXT,
            address2 TEXT,
            city TEXT,
            state TEXT,
            pincode TEXT,

            prevSchool TEXT,
            prevInstitution TEXT,
            tenthYear INTEGER,
            tenthPercentage REAL,
            twelfthYear INTEGER,
            twelfthPercentage REAL,
            entranceExam TEXT,

            courseApplied TEXT,
            specialization TEXT,
            admissionType TEXT,
            enrollment TEXT,

            FatherName TEXT,
            FatherOccupation TEXT,
            motherName TEXT,
            MotherOccupation TEXT,
            parentsContact TEXT,
            parentsEmail TEXT,
            parentsIncome REAL,

            hostel TEXT,
            transport TEXT,
            medicalCondition TEXT,

            scholarship TEXT,
            bankAccount TEXT,
            ifsc TEXT
        )
    """)
    conn.commit()
    conn.close()

# Call init once
init_db()

# ---------- ROUTES ----------
@app.route("/")
def home():
    return "<h2>Backend is running. Open form.html in browser to submit data.</h2>"

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO students (
            fullname, gender, dob, nationality, aadhar, email, phone,
            address1, address2, city, state, pincode,
            prevSchool, prevInstitution, tenthYear, tenthPercentage,
            twelfthYear, twelfthPercentage, entranceExam,
            courseApplied, specialization, admissionType, enrollment,
            FatherName, FatherOccupation, motherName, MotherOccupation,
            parentsContact, parentsEmail, parentsIncome,
            hostel, transport, medicalCondition,
            scholarship, bankAccount, ifsc
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("fullname"), data.get("gender"), data.get("dob"), data.get("nationality"),
        data.get("aadhar"), data.get("email"), data.get("phone"),

        data.get("address1"), data.get("address2"), data.get("city"),
        data.get("state"), data.get("pincode"),

        data.get("prevSchool"), data.get("prevInstitution"),
        data.get("tenthYear"), data.get("tenthPercentage"),
        data.get("twelfthYear"), data.get("twelfthPercentage"),
        data.get("entranceExam"),

        data.get("courseApplied"), data.get("specialization"),
        data.get("admissionType"), data.get("enrollment"),

        data.get("FatherName"), data.get("FatherOccupation"),
        data.get("motherName"), data.get("MotherOccupation"),
        data.get("parentsContact"), data.get("parentsEmail"),
        data.get("parentsIncome"),

        data.get("hostel"), data.get("transport"),
        data.get("medicalCondition"),

        data.get("scholarship"), data.get("bankAccount"),
        data.get("ifsc")
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Student registered successfully!"})

@app.route("/students", methods=["GET"])
def get_students():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(port=5004, debug=True)