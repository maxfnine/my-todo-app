FILEPATH="todos.txt"
def get_todos(filepath=FILEPATH):
    """Reads text file and returns list of todo items"""
    with open(filepath, 'r') as file:
        items = file.readlines()
    return items


def write_todos(filepath=FILEPATH, items=[]):
    """Writes todo items to a text file"""
    with open(filepath, 'w') as file:
        file.writelines(items)
