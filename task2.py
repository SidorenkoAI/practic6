class task2:
    def __init__(self):
        pass
    def greater(self, arg):
        if len(arg) == 0:
            return False
        res = True
        for i in range(len()):
            if arg[i] >= arg[i+1]:
                res = False
        return res


        '''
        :param arg: список целых чисел
        :return: Если arg монотонно возрастает
        (то есть каждый элемент больше предыдущего),
        то вернуть True, иначе False
        '''
