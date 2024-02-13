from bottle import default_app, error, get, redirect, static_file, template
import sqlite3 
import x

##############################
@get("/app.css")
def _():
    return static_file("app.css", ".")
 
##############################
import routes.get_users
import routes.get_items
import routes.delete_user


##############################
@get("/") # 127.0.0.1
def _():
    return template("index.html")
 
##############################
@error(404)
def _(error):
    return "page not found :("
 
##############################
@get("/signup")
def _():
    return template("signup.html")

##############################
@get("/login")
def _():
    return template("login.html")









##############################  
@get("/items/<id>")
def _(id):
    title = "Item " + id
    return template("item", 
                    id=id, 
                    title = title)





##############################
app = default_app()
 


