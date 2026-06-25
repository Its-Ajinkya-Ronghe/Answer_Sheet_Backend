from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd
import sqlite3

from flask import send_file
from flask_cors import CORS

from gemini_service import extract_data

from database import init_db
from database import save_result

import os

app = Flask(__name__)

CORS(app)

os.makedirs("uploads", exist_ok=True)

init_db()


@app.route("/extract", methods=["POST"])
def extract():

    if "image" not in request.files:

        return jsonify({
            "error": "No image"
        }), 400

    image = request.files["image"]

    image_bytes = image.read()

    result = extract_data(image_bytes)

    return jsonify(result)

@app.route("/results", methods=["GET"])
def get_results():

    import sqlite3

    conn = sqlite3.connect("database/answer_sheet.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
        registration_no,
        roll_no,
        student_name,
        course_code,
        q1_total,
        q2_total,
        q3_total,
        grand_total
        FROM results
        ORDER BY registration_no
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]

@app.route("/download-excel")
def download_excel():

    session = request.args.get("session")
    course_code = request.args.get("subject")

    conn = sqlite3.connect(
        "database/answer_sheet.db"
    )

    # query = """
    # SELECT *
    # FROM results
    # WHERE session = ?
    # AND course_code = ?
    # """

    query = """
            SELECT *
            FROM results
            """

    df = pd.read_sql_query(query, conn)

    # df = pd.read_sql_query(
    #     query,
    #     conn,
    #     params=(session, course_code)
    # )

    conn.close()

    if df.empty:

        return jsonify({
            "message": "No data found"
        }), 404

    filename = "results.xlsx"

    df.to_excel(
        filename,
        index=False
    )

    return send_file(
        filename,
        as_attachment=True,
        download_name="results.xlsx"
    )

@app.route("/save", methods=["POST"])
def save():

    data = request.json

    save_result(data)

    return jsonify({
        "message": "Saved Successfully"
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )