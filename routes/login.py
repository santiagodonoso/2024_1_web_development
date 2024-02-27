from bottle import post, response
import x

@post("/login")
def _():
    try:
        # TODO: validate the email and password
        # validate password
        x.validate_user_email()
        x.validate_user_password()

        response.set_cookie("name", "Santiago", secret="my_secret", httponly=True)
        return """
        <template mix-redirect="/admin">
        </template>
        """
    except Exception as ex:
        print(ex)
        print(type(ex))
        print(ex.args[0])
        print(ex.args[1]) # user_password xxxxx  user_email xxxxx

        if "user_password" in ex.args[1]:
            return """
            <template mix-target="#error" mix-replace>
                <div id="error">User password invalid</div>
            </template>
            """
        
        if "user_email" in ex.args[1]:
            return """
            <template mix-target="#error" mix-replace>
                <div id="error">User email invalid</div>
            </template>
            """
        
        return """
        <template mix-target="#error" mix-replace>
            <div id="error">System under maintainance</div>
        </template>
        """

    finally:
        pass





