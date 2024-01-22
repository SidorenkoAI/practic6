def MoveStrings(s, d):
    s.extend(d)
    for str in d:
        d.remove(str)
    print(s)

s = ['a','b','c','d','e','f']
d = ['ab','cd','ef']
MoveStrings(s,d)