import speech
import text
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def showHomePage():
    # user_input = input("Hello! Please choose 1 for Speech and 2 for Text.\n Choose 0 to EXIT.\n")
    # print("Your choice is: " + user_input)
    #
    # while user_input != "0":
    #
    #     if user_input == "1":
    #         speech.run()
    #         user_input = input("Hello! Please choose 1 for Text and 2 for Speech.\n Choose 0 to EXIT.\n")
    #
    #     elif user_input == "2":
    #         text.run()
    #         user_input = input("Hello! Please choose 1 for Text and 2 for Speech.\n Choose 0 to EXIT.\n")
    #
    #     else:
    #         print("Wrong input! Please try again.")
    #         user_input = input("Hello! Please choose 1 for Text and 2 for Speech.\n Choose 0 to EXIT.\n")

    return "This is home page"


@app.route("/test", methods=["POST"])
def test():
    text_test = request.form["test"]
    print(text_test)
    text.run(text_test)
    return "received"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
