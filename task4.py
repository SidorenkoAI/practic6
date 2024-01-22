def PalindromeFilter(arg, minLength):
    Palendrom = list()
    for k in arg:
        if len(k) >= minLength:
            Rev = k[::-1]
            if Rev == k:
                Palendrom.append(k)
    return  Palendrom