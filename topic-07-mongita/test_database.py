# test_database.py - functions for testing database.py

from mongita_database import get_items, add_item, delete_item, update_item

def test_get_items():
    print("testing get_items...")
    items = get_items()
    assert type(items) is list
    assert len(items) > 0
    assert type(items[0]) is dict
    assert 'id' in items[0].keys()
    assert 'description' in items[0].keys()
    assert type(items[0]['id']) is str
    assert type(items[0]['description']) is str
    items = get_items(items[0]['id'])
    assert type(items) is list
    assert len(items) == 1
    assert type(items[0]) is dict
    assert 'id' in items[0].keys()
    assert 'description' in items[0].keys()
    assert type(items[0]['id']) is str
    assert type(items[0]['description']) is str


import time

def random_string():
    return str(time.time())

def test_add_item():
    print("testing add_item...")
    description = random_string()
    add_item(description)
    items = get_items()
    item = items[-1]
    assert description == item['description']
    delete_item(item['id'])

def test_delete_item():
    print("testing delete_item...")
    description = random_string()
    add_item(description)
    items = get_items()
    item = items[-1]
    assert description == item['description']
    delete_item(item['id'])
    items = get_items()
    for item in items:
        assert description != item['description']

def test_update_item():
    print("testing update_item...")
    description = random_string()
    add_item(description)
    items = get_items()
    item = items[-1]
    id = str(item['id'])
    description = item['description']
    new_description = description.replace("1","9").replace(".",":")
    update_item(id, new_description)
    items = get_items()
    new_found = False
    for item in items:
        if item['id'] == id:
            assert item['description'] == new_description
            delete_item(item['id'])
            new_found = True
        assert item['description'] != description
    assert new_found

if __name__ == "__main__":
    test_get_items()
    test_add_item()
    test_delete_item()
    test_update_item()
    print("done.")



