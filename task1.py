class task1:
    def __init__(self):
        pass
    def giveEvenNumbers(self, arg):
        evennumbers = []
        for i in arg:
            if i % 2 == 0:
                evennumbers.append(i)
        print(evennumbers)

a = [1,2,3,4,5,6,7,8,9,10]
task1.giveEvenNumbers(1,a)
