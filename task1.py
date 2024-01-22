class task1:
    def __init__(self):
        pass
    def giveEvenNumbers(self, arg):
        evnum = list()
        for i in arg:
            if i % 2 == 0:
                evnum.append(i)
        return evnum

