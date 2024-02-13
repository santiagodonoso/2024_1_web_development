from bottle import get, redirect
import x

##############################  
@get("/delete-user/<uuid>")
def _(uuid):
    db = x.db()
    sql = db.execute(f"""
                     DELETE FROM users 
                     WHERE user_pk = '{uuid}'
                    """)
    db.commit()
    redirect("/users")