from bottle import delete
import x

##############################
@delete("/items/<id>")
def _(id):
    try:
        db = x.db()
        q = db.execute("DELETE FROM items WHERE item_id = ?", (id,))
        db.commit()
        return f"item deleted with id: {id}"
    except Exception as ex:
        print(ex)
    finally:
        if "db" in locals(): db.close()