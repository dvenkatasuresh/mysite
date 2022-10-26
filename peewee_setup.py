from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('peewee_shopping_list.db')

class Item(Model):
    description = CharField()

    class Meta:
        database = db

def add_items_to_db():
    global db
    items = [
        { "description": 'apples' },
        { "description": 'broccoli' },
        { "description": 'pizza' },
        { "description": 'tangerine' },
        { "description": 'potatoes' }
        ]
    for item in items:
        Item.create(description=item['description'])
    print(items)
if __name__ == "__main__":
    db.connect()
    db.create_tables([Item])
    add_items_to_db()