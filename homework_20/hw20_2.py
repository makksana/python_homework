import sys
print('Task 2', end='\n\n')
# The sys module.

# The “sys.path” list is initialized
# from the PYTHONPATH environment variable.
# Is it possible to change it from within Python?
# If so, does it affect where Python looks for module files?
# Run some interactive tests to find it out.


def print_path():
    print(sys.path)


def add_path(path, index=0):
    sys.path.insert(index, path)


def delete_path(path):
    sys.path.remove(path)


if __name__ == '__main__':
    print_path()
    add_path('~/Downloads/python', 2)
    print_path()
    delete_path('~/Downloads/python')
    print_path()
