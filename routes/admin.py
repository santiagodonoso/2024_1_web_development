from bottle import get, request

@get("/admin")
def _():
    name = request.get_cookie("name")
    return f"Hi {name}"