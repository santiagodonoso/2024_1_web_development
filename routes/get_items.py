from bottle import get, template


##############################  
@get("/items")
def _():
    try:
        box = [] # list and it is empty
        for i in range(1, 101):
            box.append(i)
        print(box)    
        return template("items", box=box)   
    except Exception as ex:
        print(ex)
        return "error"
    finally:
        pass










    
