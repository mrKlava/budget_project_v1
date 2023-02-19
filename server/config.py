from dotenv import load_dotenv
import os
import redis

load_dotenv()

class ApplicationConfig:
  # import secret key from environment variables
  SECRET_KEY = os.environ["SECRET_KEY"]
  # disable logs 
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  # log called queries
  SQLALCHEMY_ECHO = True
  # connect db !!! check how it is written
  SQLALCHEMY_DATABASE_URI = r"sqlite:///../db/budget.db"

  SESSION_TYPE = "redis"
  SESSION_PERNAMENT = False
  SESSION_USE_SIGNER = True
  SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")