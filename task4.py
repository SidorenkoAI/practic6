
def PalindromeFilter(arg, minLength):
    palind = []
    palindmin = []
    for i in arg:
        if i == i[::-1]:
          palind.append(i)
    for n in palind:
        if len(n) >= minLength:
            palindmin.append(n)
    print(palindmin)
