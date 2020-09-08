def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lst = phrase.split()
    lst = [word.capitalize() for word in lst]
    p = " "
    return p.join(lst)

print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))