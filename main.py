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

if __name__ == "__main__":
    app.run(host="0.0.0.0")
