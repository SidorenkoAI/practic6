class task1:
    def __init__(self):
        pass
    def giveEvenNumbers(self, arg):
        spisok = list()
        for num in arg:
            if num % 2 == 0:
                spisok.append(num)
        return spisok


        ''':param arg: список целых чисел
        :return: список четных чисел
        '''
