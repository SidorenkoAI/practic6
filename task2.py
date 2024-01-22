class task2:
    def __init__(self):
        pass
    def greater(self, arg):
        vozr = list()
        for num in len(arg):
            if arg[num] < arg[num+1]:
                return True
            else: return False


        '''
        :param arg: список целых чисел
        :return: Если arg монотонно возрастает
        (то есть каждый элемент больше предыдущего),
        то вернуть True, иначе False
        '''
