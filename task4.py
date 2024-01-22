def PalindromeFilter(arg, minLength):
    '''
    :param arg: список строк
    :return: список строк, которые являются
    палиндромами и имеют длину не меньше minLength
    '''
    arg = arg.replace(' ','').lower()
    return arg if (arg == arg[::-1] and len(arg) > minLength) else "False"
a = PalindromeFilter("калаш", 5)
print(a)
