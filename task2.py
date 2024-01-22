class task2:
    def __init__(self):
        pass
    def greater(self, arg):
        vozr = list()
        for num in len(arg):
            if arg[num] > arg[num+1]:
                print("всё норм")
            else: print("не то")


        '''
        :param arg: список целых чисел
        :return: Если arg монотонно возрастает
        (то есть каждый элемент больше предыдущего),
        то вернуть True, иначе False
        '''
