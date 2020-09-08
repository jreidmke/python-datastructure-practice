def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    lst2 = [el for el in lst if bool(el) == True]
    return lst2

print(compact([0, 1, 2, '', [], False, (), None, 'All done']))