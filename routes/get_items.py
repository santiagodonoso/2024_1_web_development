from bottle import get, template
import x

##############################  
@get("/items")
def _():
    try:
       db = x.db()
       return "x"
    except Exception as ex:
       print(ex)
    finally:
       if "db" in locals(): db.close()










    
