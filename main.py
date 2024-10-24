import os

import speech
import text
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def showHomePage():

    return "This is home page"

@app.route("/test", methods=["POST"])
def test():
    text_test = request.form["test"]
    result = text.run(text_test)
    return result


UPLOAD_FOLDER = './uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        return speech.speech()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
