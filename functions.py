FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return a list of
    to-do items
    """
    with open(filepath, 'r') as file_:
        """ write the to-do list to a text file"""
        todos_ = file_.readlines()
    return todos_


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
