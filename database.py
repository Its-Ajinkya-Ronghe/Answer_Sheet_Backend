import sqlite3
import os

DB_PATH = "database/answer_sheet.db"


def init_db():

    os.makedirs("database", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results(

        registration_no TEXT PRIMARY KEY,

        roll_no TEXT,

        student_name TEXT,

        branch TEXT,
        section TEXT,

        session TEXT,
        subject TEXT,

        course_code TEXT,

        q1a INTEGER,
        q1b INTEGER,
        q1c INTEGER,

        q2a INTEGER,
        q2b INTEGER,
        q2c INTEGER,

        q3a INTEGER,
        q3b INTEGER,
        q3c INTEGER,

        q1_total INTEGER,
        q2_total INTEGER,
        q3_total INTEGER,

        grand_total INTEGER
    )
    """)

    conn.commit()
    conn.close()


def save_result(data):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO results(

        registration_no,
        roll_no,
        student_name,

        branch,
        section,

        session,
        subject,

        course_code,

        q1a,
        q1b,
        q1c,

        q2a,
        q2b,
        q2c,

        q3a,
        q3b,
        q3c,

        q1_total,
        q2_total,
        q3_total,

        grand_total

    ) VALUES(

        ?,?,?,?,?,?,
        ?,?,
        ?,
        ?,?,?,
        ?,?,?,
        ?,?,?,
        ?,?,?,
        ?

    )
    """, (

        data["registration_no"],
        data["roll_no"],
        data["student_name"],

        data["branch"],
        data["section"],

        data["session"],
        data["subject"],

        data["course_code"],

        data["q1a"],
        data["q1b"],
        data["q1c"],

        data["q2a"],
        data["q2b"],
        data["q2c"],

        data["q3a"],
        data["q3b"],
        data["q3c"],

        data["q1_total"],
        data["q2_total"],
        data["q3_total"],

        data["grand_total"]

    ))

    conn.commit()
    conn.close()