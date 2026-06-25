import sqlite3
import os

DB_PATH = "database/answer_sheet.db"


def init_db():

    os.makedirs("database", exist_ok=True)

    # DELETE OLD DATABASE (for development only)
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE results(

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

        data.get("registration_no", ""),
        data.get("roll_no", ""),
        data.get("student_name", ""),

        data.get("branch", ""),
        data.get("section", ""),

        data.get("session", ""),
        data.get("subject", ""),

        data.get("course_code", ""),

        data.get("q1a", 0),
        data.get("q1b", 0),
        data.get("q1c", 0),

        data.get("q2a", 0),
        data.get("q2b", 0),
        data.get("q2c", 0),

        data.get("q3a", 0),
        data.get("q3b", 0),
        data.get("q3c", 0),

        data.get("q1_total", 0),
        data.get("q2_total", 0),
        data.get("q3_total", 0),

        data.get("grand_total", 0)

    ))

    conn.commit()
    conn.close()