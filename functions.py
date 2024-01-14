FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = [line.strip() for line in file_local.readlines()]
    return todos_local


def write_todos(todo_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as fil_local:
        file_contents = '\n'.join(todo_arg)
        fil_local.write(file_contents)



if __name__ == "__main__":
    print("Hello")
    print(get_todos())
