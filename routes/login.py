from bottle import post, response

@post("/login")
def _():
    # TODO: validate the email and password
    response.set_cookie("name", "Santiago")
    return """
    <template mix-redirect="/admin">
    </template>
    """





