def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    r_vowel_list = list(reversed([c for c in s if c in 'aeiou' or c in "AEIOU"]))
    s_lst = list(s)

    count = 0
    for i in range(len(s_lst)):
        if s_lst[i] in 'aeiou' or s_lst[i] in "AEIOU":
            print(s_lst[i], r_vowel_list[count])
            s_lst[i] = r_vowel_list[count]
            count += 1

    return "".join(s_lst)
