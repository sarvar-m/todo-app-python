def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todo_arg, filepath="todos.txt" ):
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as fil_local:
        fil_local.writelines(todo_arg)