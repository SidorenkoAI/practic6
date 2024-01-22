def PalindromeFilter(arg, minLength):
    palinlist = []
    for word in arg:
        if word == word[::-1]:
            if len(word) > minLength:
                palinlist.append(word)
    print(palinlist)

