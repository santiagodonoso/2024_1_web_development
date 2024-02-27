from bottle import request
import sqlite3
import pathlib
import re

##############################
def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

##############################
def db():
    try:
        db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/database/company.db")
        db.execute("PRAGMA foreign_keys = ON")
        db.row_factory = dict_factory # JSON objects
        return db
    except Exception as ex:
        print("db function has an errror")
        print(ex)
    finally:
        pass

##############################
USER_NAME_MIN = 2
USER_NAME_MAX = 20

def validate_user_name():
    if len(request.forms.get("user_name")) < USER_NAME_MIN: 
        raise Exception("name too short")
    if len(request.forms.get("user_name")) > USER_NAME_MAX: 
        raise Exception("name too long")
    # SUCCESS
    return "ok"



##############################
USER_LAST_NAME_MIN = 2
USER_LAST_NAME_MAX = 20

def validate_user_last_name():
    if len(request.forms.get("user_last_name")) < USER_LAST_NAME_MIN: 
        raise Exception("last name too short")
    if len(request.forms.get("user_last_name")) > USER_LAST_NAME_MAX: 
        raise Exception("last name too long")
    # SUCCESS
    return "ok"


##############################
USER_PASSWORD_MIN = 6
USER_PASSWORD_MAX = 50
USER_PASSWORD_REGEX = "^.{6,50}$"

def validate_user_password():
    error = f"user_password {USER_PASSWORD_MIN} to {USER_PASSWORD_MAX} characters"
    user_password = request.forms.get("user_password", "")
    user_password = user_password.strip()
    # if len(user_password) < USER_PASSWORD_MIN : raise Exception(400, error)
    # if len(user_password) > USER_PASSWORD_MAX : raise Exception(400, error)
    if not re.match(USER_PASSWORD_REGEX, user_password): raise Exception(400, error)
    return user_password


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







