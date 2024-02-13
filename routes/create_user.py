from bottle import post, request
import x

##############################
@post("/users")
def _():
    try:
         # Design by contract between front and back-end
        # VALIDATION
        x.validate_user_name()
        x.validate_user_last_name()

        user_name = request.forms.get("user_name")
        user_last_name = request.forms.get("user_last_name")
        # Show Hi A Aa
        return f"Hi {user_name} {user_last_name}"
    except Exception as ex:
        print(ex)
    finally:
        pass





