class task1:
    def __init__(self):
        pass
    def giveEvenNumbers(self, arg):
        numbers = list()
        for num in arg:
            if num % 2 == 0:
                numbers.append(num)
        return numbers