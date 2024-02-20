from bottle import request
import sqlite3
import pathlib

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











