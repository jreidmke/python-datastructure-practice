def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    commands = ['add', 'remove']
    locations = ['beginning', 'end']

    if command not in commands:
        return None

    if location not in locations:
        return None


    if command == 'remove':
        if location.startswith('b'):
            return lst[0]
        else:
            return lst[-1]

    if command == 'add':
        if location.startswith('b'):
            lst.insert(0, value)
            return lst
        else:
            lst.insert(-1, value)
            return lst

lst = [1, 2, 3]
print(list_manipulation(lst, 'remove', 'end'))
print(list_manipulation(lst, 'remove', 'beginning'))
print(list_manipulation(lst, 'add', 'beginning', 20))
print(list_manipulation(lst, 'add', 'end', 30))
print(list_manipulation(lst, 'foo', 'end'))
print(list_manipulation(lst, 'add', 'dunno'))