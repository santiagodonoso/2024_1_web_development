from bottle import post, request
import x

@post("/signup")
def _():
    try:
        # Validate
        x.validate_user_email()

        return """
        <template>
        </template>
        """
    except Exception as ex:
        print(ex)
        if "user_email" in ex.args[1]:
            return """
            <template mix-target="#message">
            <div id="message">
                Email invalid
            </div>
            </template>    
            """
    finally:
        pass