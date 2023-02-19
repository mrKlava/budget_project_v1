from flask_sqlalchemy import SQLAlchemy
#  create unique id
from uuid import uuid4

# us
db = SQLAlchemy()


# create unique user id
def get_uuid():
	return uuid4().hex


# this is user model -> Constructor will create table users
class User(db.Model):
	# name of table
	__tablename__ = "users"
	# unique id
	id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
	email = db.Column(db.String(345), unique=True)
	hash = db.Column(db.Text, nullable=False)
