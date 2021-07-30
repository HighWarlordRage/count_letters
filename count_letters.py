#Title: Project-8a
def count_letters(m):
    """ a function named count_letters that takes as a parameter a string
    and returns a dictionary that tabulates how many of each letter is in that string. """
    n = {}
    for cl in m:
        cl = cl.upper()
        if 'A' <= cl <= 'Z':
            if cl not in n:
                n[cl] = 0
            n[cl] += 1
    return n

#print(count_letters("AaBb"))