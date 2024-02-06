from bottle import default_app, error, get, static_file, template
 
##############################
@get("/app.css")
def _():
    return static_file("app.css", ".")
 
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
@get("/items")
def _():
    return template("items")   

##############################  
@get("/items/<id>")
def _(id):
    return template("item")






##############################
app = default_app()
 


