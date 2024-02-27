from bottle import get, request, template
import x

@get("/admin")
def _():
    x.disable_cache() # browser do not remember this page < >
    name = request.get_cookie("name", secret="my_secret")
    if name:
        return template("admin", name=name)
    else:
        return "access denied"