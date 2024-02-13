from bottle import post, request
import x

##############################
@post("/users")
def _():
    try:
        # VALIDATION
        user_name = request.forms.get("user_name")
        user_last_name = request.forms.get("user_last_name")
        # Show Hi A Aa
        return f"Hi {user_name} {user_last_name}"
    except Exception as ex:
        print(ex)
    finally:
        pass





