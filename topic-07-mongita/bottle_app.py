from bottle import default_app, route, get, post, template, request, redirect

from mongita_database import get_items, add_item, delete_item, update_item

@route('/')
def get_index():
    redirect('/list')

@route('/list')
def get_list():
    items = get_items()
    return template("shopping_list.tpl", name="Dr. DeLozier", shopping_list=items)

@post('/add')
def post_add():
    description = request.forms.get("description")
    # quantity = request.forms.get("quantity")
    # try:
    #     quantity = int(quantity)
    # except:
    #     quantity = 1
    # add_item(description, quantity)
    add_item(description)
    redirect('/list')

@route("/delete/<id>")
def get_delete(id):
    delete_item(id)
    redirect('/list')

@get("/edit/<id>")
def get_edit(id):
    items = get_items(id)
    if len(items) != 1:
        redirect('/list')
    item_id, description = items[0]['id'], items[0]['description']
    assert item_id == id
    return template("edit_item.tpl", id=id, description=description)

@post("/edit/<id>")
def post_edit(id):
    description = request.forms.get("description")
    update_item(id, description)
    redirect('/list')

application = default_app()

