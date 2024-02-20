from bottle import post, request

##############################
@post("/items")
def _():
    try:
        item_name = request.forms.get("item_name")

        return f"""
        <template mix-target="#items" mix-top>
            <div>
                {item_name}
            </div> 
        </template>
        """
    except Exception as ex:
        pass
    finally:
        pass
