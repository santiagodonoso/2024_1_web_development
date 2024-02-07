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
    box = [] # list and it is empty
    for i in range(1, 101):
        box.append(i)
    print(box)    
    return template("items", box=box)   

##############################  
@get("/users")
def _():
    box = [
        {"user_pk":"1", "user_name":"A"},
        {"user_pk":"2", "user_name":"B"},
    ]
    # for i in range(1, 11):
    #     box.append(i)
    # print(box)    
    return template("users", box=box)   


##############################  
@get("/items/<id>")
def _(id):
    title = "Item " + id
    return template("item", 
                    id=id, 
                    title = title)





##############################
app = default_app()
 


