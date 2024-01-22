class task2:
    def __init__(self):
        pass
    def greater(self, arg):
        """
        :param arg: список целых чисел
        :return: Если arg монотонно возрастает
        (то есть каждый элемент больше предыдущего),
        то вернуть True, иначе False
        """
        i = 1
        while i <= len(arg) - 1 and arg[i] > arg[i - 1]:
            i += 1
        return 'YES' if i == len(arg) else 'NO'
        