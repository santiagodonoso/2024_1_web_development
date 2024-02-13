from bottle import get, redirect
import x

##############################  
@get("/delete-user/<uuid>")
def _(uuid):
    try:
        db = x.db()
        sql = db.execute(f"""
                        DELETE FROM users 
                        WHERE user_pk = '{uuid}'
                        """)
        db.commit()
        redirect("/users")
    except Exception as ex:
        print(ex)
        return "error"
    finally:
        if "db" in locals(): db.close()