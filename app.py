from flask import Flask, request
import json


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world", 200


@app.route("/user")
def user():
    name = request.json.get("name")
    return "Hello {}".format(name), 200


@app.route("/my_name")
def name():
    return "my name is Chijiuba Onyedikachukw"



# if __name__ == "__main__":
#     app.run(debug=True)
