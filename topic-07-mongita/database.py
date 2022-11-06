# database.py - functions for managing database

import sqlite3

connection = sqlite3.connect("shopping_list.db")

def get_items(id=None):
    cursor = connection.cursor()
    if id:
        items = cursor.execute(f"select id, description from list where id={id}")
    else:
        items = cursor.execute("select id, description from list")
    items = list(items)
    items = [ {'id':item[0] ,'description':item[1]} for item in items ]
    return items

def add_item(description):
    cursor = connection.cursor()
    cursor.execute(f"insert into list (description) values ('{description}')")
    connection.commit()

def delete_item(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from list where id={id}")
    connection.commit()

def update_item(id, description):
    cursor = connection.cursor()
    cursor.execute(f"update list set description='{description}' where id={id}")
    connection.commit()

