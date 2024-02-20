from bottle import request, response
import sqlite3
import re
import pathlib

COOKIE_SECRET = "41ebeca46feb-4d77-a8e2-554659074C6319a2fbfb-9a2D-4fb6-Afcad32abb26a5e0"

##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

##############################
def db():
	try:
		db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
		db.execute("PRAGMA foreign_keys=ON")
		db.row_factory = dict_factory
		return db
	except Exception as ex:
		print(ex)
	finally:
		pass

##############################
def get_values_from_dictionary(dictionary):
	values = ""
	for key in dictionary:
		values += f":{key},"
	return values.rstrip(",")	

##############################
def disable_cache():
    response.add_header("Cache-Control", "no-cache, no-store, must-revalidate")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)    

##############################
def validate_user_logged():
    user = request.get_cookie("user", secret=COOKIE_SECRET)
    if user is None: raise Exception(400, "user must login")
    return user

##############################

USER_ID_LEN = 32
USER_ID_REGEX = "^[a-f0-9]{32}$"

def validate_user_id():
	error = f"user_id invalid"
	user_id = request.forms.get("user_id", "")        
	user_id = user_id.strip()
	if len(user_id) != USER_ID_LEN : raise Exception(400, error)
	if not re.match(USER_ID_REGEX, user_id): raise Exception(400, error)
	return user_id

def validate_user_follower_id():
	error = f"user_follower_id invalid"
	user_follower_id = request.forms.get("user_follower_id", "")        
	user_follower_id = user_follower_id.strip()
	if len(user_follower_id) != USER_ID_LEN : raise Exception(400, error)
	if not re.match(USER_ID_REGEX, user_follower_id): raise Exception(400, error)
	return user_follower_id

def validate_user_followee_id():
	error = f"user_followee_id invalid"
	user_followee_id = request.forms.get("user_followee_id", "")        
	user_followee_id = user_followee_id.strip()
	if len(user_followee_id) != USER_ID_LEN : raise Exception(400, error)
	if not re.match(USER_ID_REGEX, user_followee_id): raise Exception(400, error)
	return user_followee_id


##############################

USER_EMAIL_MIN = 6
USER_EMAIL_MAX = 100
USER_EMAIL_REGEX = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"

def validate_user_email():
	error = f"user_email invalid"
	user_email = request.forms.get("user_email", "")        
	user_email = user_email.strip()
	if len(user_email) < USER_EMAIL_MIN : raise Exception(400, error)
	if len(user_email) > USER_EMAIL_MAX : raise Exception(400, error)  
	if not re.match(USER_EMAIL_REGEX, user_email): raise Exception(400, error)
	return user_email

##############################

USER_NAME_MIN = 2
USER_NAME_MAX = 20
USER_NAME_REGEX = "^[a-z0-9]{2,20}$"

def validate_user_name():
	error = f"user_name {USER_NAME_MIN} to {USER_NAME_MAX} lowercased english letters"
	user_name = request.forms.get("user_name", "")
	user_name = user_name.strip()
	if not re.match(USER_NAME_REGEX, user_name): raise Exception(400, error)
	return user_name


##############################

USER_PHONE_LEN = 8
USER_PHONE_REGEX = "^[1-9][0-9]{7}$"

def validate_user_phone():
	error = f"user_phone must be {USER_PHONE_LEN} numbers. Cannot start with 0"
	user_phone = request.forms.get("user_phone", "")
	user_phone = user_phone.strip()
	if not re.match(USER_PHONE_REGEX, user_phone): raise Exception(400, error)
	return user_phone

##############################

USER_FIRST_NAME_MIN = 2
USER_FIRST_NAME_MAX = 20

def validate_user_first_name():
	error = f"user_first_name {USER_FIRST_NAME_MIN} to {USER_FIRST_NAME_MAX} characters"
	user_first_name = request.forms.get("user_first_name", "")
	user_first_name = user_first_name.strip()
	if len(user_first_name) < USER_FIRST_NAME_MIN : raise Exception(400, error)
	if len(user_first_name) > USER_FIRST_NAME_MAX : raise Exception(400, error)
	return user_first_name

##############################

USER_PASSWORD_MIN = 6
USER_PASSWORD_MAX = 50

def validate_user_password():
	error = f"user_password {USER_PASSWORD_MIN} to {USER_PASSWORD_MAX} characters"
	user_password = request.forms.get("user_password", "")
	user_password = user_password.strip()
	if len(user_password) < USER_PASSWORD_MIN : raise Exception(400, error)
	if len(user_password) > USER_PASSWORD_MAX : raise Exception(400, error)
	return user_password

def validate_user_confirm_password():
	error = f"user_password and user_confirm_password do not match"
	user_password = request.forms.get("user_password", "")
	user_confirm_password = request.forms.get("user_confirm_password", "")
	user_password = user_password.strip()
	user_confirm_password = user_confirm_password.strip()
	if user_confirm_password != user_password: raise Exception(400, error)
	return user_confirm_password

##############################

TWEET_MIN_LEN = 2
TWEET_MAX_LEN = 100

def validate_tweet_message():
	error = f"tweet_message {TWEET_MIN_LEN} to {TWEET_MAX_LEN} characters"
	tweet_message = request.forms.get("tweet_message", "")
	tweet_message = tweet_message.strip()
	if len(tweet_message) < TWEET_MIN_LEN : raise Exception(400, error)
	if len(tweet_message) > TWEET_MAX_LEN : raise Exception(400, error)
	return tweet_message

##############################






