class task1:
    def __init__(self):
        pass
    def giveEvenNumbers(self, arg):
        evennumbers = []
        for i in arg:
            if i % 2 == 0:
                evennumbers.append(i)
        print(evennumbers)
