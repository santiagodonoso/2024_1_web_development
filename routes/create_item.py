from bottle import post, request
import uuid
import random
import x

##############################
@post("/items")
def _():
    try:
        item_name = request.forms.get("item_name")
        item_id = uuid.uuid4().hex
        item_price = random.uniform(10.5, 999.99)
        db = x.db()
        q = db.execute("INSERT INTO items VALUES(?, ?, ?)", (item_id, item_name, item_price))
        db.commit()
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
