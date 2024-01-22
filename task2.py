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
        if len(arg) <= 1:
            return True

        for i in range(len(arg) - 1):
            if arg[i] >= arg[i + 1]:
                return False

        return True