class task1:
    def __init__(self):
        pass
    def giveEvenNumbers(self, arg):
        EvNum = list()
        for num in arg:
            if num % 2 == 0:
                EvNum.append(num)
        return EvNum
