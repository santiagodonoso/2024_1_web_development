from bottle import post, request
import x

##############################
@post("/users")
def _():
    try:
        # VALIDATION
        user_name = request.forms.get("user_name")
        return f"Hi {user_name}"
    except Exception as ex:
        print(ex)
    finally:
        pass





