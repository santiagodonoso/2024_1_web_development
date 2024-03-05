from bottle import post, request
import x
import uuid

@post("/signup")
def _():
    try:
        # Validate
        user_email = x.validate_user_email()
        user_id = uuid.uuid4().hex
        user_name = "Santiago"
        user_updated_at = 0
        user_password = "password"

        db = x.db()
        q = db.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?)", 
                       (user_id, user_name, user_updated_at, user_email, user_password))
        db.commit()
        return """
        <template mix-target="#message">
            <div id="message">
                User created
            </div>        
        </template>
        """
    except Exception as ex:
        print(ex)
        if "users.user_email" in str(ex):
             return """
            <template mix-target="#message">
            <div id="message">
                Email not available
            </div>
            </template>    
            """           


        if "user_email invalid" in str(ex):
            return """
            <template mix-target="#message">
            <div id="message">
                Email invalid
            </div>
            </template>    
            """
    finally:
        if "db" in locals(): db.close()