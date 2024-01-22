def PalindromeFilter(arg, minLength):

    pol = []
    for i in arg:
        prov = i[::-1]
        if prov == i:
            if len(i) >= minLength:
                pol.append(i)
    return pol

