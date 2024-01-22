class task2:
    def __init__(self):
        pass
    def greater(self, arg):
        '''
        :param arg: список целых чисел
        :return: Если arg монотонно возрастает
        (то есть каждый элемент больше предыдущего),
        то вернуть True, иначе False
        '''

        for i in len(arg):
            if i + 1 != len(arg):
                if arg[i] < arg[i + 1]:
                    res = True
                else:
                    res = False
                    return res

