from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS
# from hmac import compare_digest

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


jwt = JWTManager(app)
# db = SQLAlchemy(app)


@app.route("/")
def index():
    return "Hello world", 200



# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(msg="Logged in Successfuly", token=access_token), 200



# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user, name="Asuzu Akachukwu"), 200


@app.route("/user")
def user():
    name = request.json.get("name")
    return "Hello {}".format(name), 200


@app.route("/my_name")
# @jwt_required()
def name():
    return "my name is Chijiuba Onyedikachukwu", 200



if __name__ == "__main__":
    app.run(debug=True)

