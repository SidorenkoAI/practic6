class task2:
    def __init__(self):
        pass
    def greater(self, arg):
        IsUp = False
        for k in len(arg):
            if k + 1 != len(arg):
                if arg[k] < arg[k + 1]:
                    IsUp = True
                else:
                    IsUp = False
                    return IsUp
        return IsUp
print(task2.greater([1, 2, 3, 4, 5]))