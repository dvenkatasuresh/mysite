import sqlite3

# DB-API spec for talking to relational databases in Python

connection = sqlite3.connect("shopping_list.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list (id integer primary key, description text)")

cursor.execute("insert into list (description) values ('apples')")
cursor.execute("insert into list (description) values ('broccoli')")
cursor.execute("insert into list (description) values ('pizza')")
cursor.execute("insert into list (description) values ('tangerine')")
cursor.execute("insert into list (description) values ('potatoes')")

connection.commit()
connection.close()

print("done.")
