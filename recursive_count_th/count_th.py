# '''
# Your function should take in a single parameter (a string `word`)
# Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
# Your function must utilize recursion. It cannot contain any loops.
# '''


def count_th(word, place=0):
    if len(word) == 0:
        return 0
    if place > len(word) or place + 2 > len(word):
        return 0

    th = 0
    if word[place:place + 2] == "th":  # looks at the index 0 and 1 spot initially
        th += 1

    # place + 2 makes sure that you look at the NEXT 2 places of the string
    return th + count_th(word, place + 1)


print(count_th("thththth"))
print(count_th("abcthefthghith"))
print(count_th("abcthxyz"))
print(count_th("thhtthht"))
print(count_th("THtHThth"))
