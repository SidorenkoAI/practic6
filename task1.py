class task1:
    def __init__(self):
        pass
    def giveEvenNumbers(self, arg):

    '''
    :param arg: список целых чисел
    :return: список четных чисел
    '''
    chisl = list()
    for num in arg:
        if num % 2 == 0:
            chisl.append(num)
        return chisl