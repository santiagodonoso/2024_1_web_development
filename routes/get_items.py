from bottle import get, template
import x

##############################  
@get("/items")
def _():
    try:
        db = x.db()
        q = db.execute("SELECT * FROM items")
        items = q.fetchall()
        print(items)
        return template("items", items=items)
    except Exception as ex:
        print(ex)
    finally:
        if "db" in locals(): db.close()










    
