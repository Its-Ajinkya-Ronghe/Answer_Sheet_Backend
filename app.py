from flask import Flask
from flask import request
from flask import jsonify

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