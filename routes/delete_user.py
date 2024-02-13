from bottle import get, response
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
        response.status = 303
        response.set_header("Location", "/users")
    except Exception as ex:
        print(ex)
        return "error xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    finally:
        if "db" in locals(): db.close()
