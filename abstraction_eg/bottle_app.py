from bottle import default_app, route, get, post, template, request, redirect

import database

@route('/')
def get_index():
    redirect('/list')

@route('/list')
def get_list():
    items = database.get_items()
    return template("shoppinglist.tpl", name="DV Suresh", shopping_list=items)

@post('/add')
def post_add():
    description = request.forms.get("description")
    database.add_item(description)
    redirect('/list')

@route("/delete/<id>")
def get_delete(id):
    database.delete_item(id)
    redirect('/list')

@get("/edit/<id>")
def get_edit(id):
    items = database.get_items(id)
    if len(items) != 1:
        redirect('/list')
    item_id, description = items[0]['id'], items[0]['desc']
    assert item_id == int(id)
    return template("edititem.tpl", id=id, description=description)

@post("/edit/<id>")
def post_edit(id):
    description = request.forms.get("description")
    database.update_item(id, description)
    redirect('/list')

application = default_app()
