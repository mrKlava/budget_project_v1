from flask import Flask, request, jsonify, session
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask_cors import CORS, cross_origin
from config import ApplicationConfig
from models import db, User

# create app
app = Flask(__name__)
app.config.from_object(ApplicationConfig)

# add Bcrypt to app
bcrypt = Bcrypt(app)

# add Session to app
server_session = Session(app)

# add cors to app
CORS(app, supports_credentials=True)

# config db
db.init_app(app)

with app.app_context():
    db.create_all()


# this is route is needed to check if user is logged in 
@app.route("/@me")
def get_current_user():
    # get user from session
    user_id = session.get('user_id')

    # if no user is sign in than return error
    if not user_id:
        return jsonify({"error": "You must login"}), 409

    # get user info and return json with info
    user = User.query.filter_by(id=user_id).first()
    return jsonify({
        "id": user.id,
        "email": user.email
    })


@app.route('/')
def home():
    return {"hello": "world"}


@app.route('/register', methods=["POST"])
def register_user():

    # get payload
    email = request.json["email"]
    password = request.json["password"]

    # will make query to db to search for a user using email
    user_exists = User.query.filter_by(email=email).first() is not None

    # if user exists abort
    if user_exists:
        return jsonify({"error": "user already exists"}), 409

    # create hash
    hash = bcrypt.generate_password_hash(password)

    # create user
    new_user = User(email=email, hash=hash)
    db.session.add(new_user)
    db.session.commit()

    session["user_id"] = new_user.id

    return jsonify({
        "id": new_user.id,
        "email": new_user.email
    })


@app.route('/login', methods=["POST"])
def login_user():

    # get payload
    email = request.json["email"]
    password = request.json["password"]

    # will make query to db to search for a user using email
    user = User.query.filter_by(email=email).first()

    # if user exists abort
    if user is None:
        return jsonify({"error": "Unauthorized", "msg": "User dose not exist"}), 401

    # check entered pas with hash from table - return if wrong
    if not bcrypt.check_password_hash(user.hash, password):
        return jsonify({"error": "Unauthorized", "msg": "Wrong password"}), 401

    # add user id to session
    session["user_id"] = user.id

    # return JSON
    return jsonify({
        "id": user.id,
        "email": user.email
    })


@app.route('/logout', methods=["POST"])
def logout_user(): 
    session.pop("user_id")
    return "200"

if __name__ == "__main__":
    app.run(debug=True)
