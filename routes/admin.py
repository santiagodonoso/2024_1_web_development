from bottle import get, request, template

@get("/admin")
def _():
    name = request.get_cookie("name", secret="my_secret")
    if name:
        return template("admin", name=name)
    else:
        return "access denied"