from bottle import get, template


##############################  
@get("/items")
def _():
    box = [] # list and it is empty
    for i in range(1, 101):
        box.append(i)
    print(box)    
    return template("items", box=box)   