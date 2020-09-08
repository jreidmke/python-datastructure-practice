def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    temp = [el for el in lst if type(el) != list]
    if(temp):
        return False
    else:
        return True
