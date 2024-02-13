from bottle import get, template

##############################  
@get("/items/<id>")
def _(id):
    title = "Item " + id
    return template("item", 
                    id=id, 
                    title = title)
