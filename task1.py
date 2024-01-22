class Task1:
    def __init__(self):
        pass

    def giveEvenNumbers(self, arg):
        '''
        :param arg: список целых чисел
        :return: список четных чисел
        '''
        even_numbers = [num for num in arg if num % 2 == 0]
        return even_numbers

task = Task1()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = task.giveEvenNumbers(numbers)
print(result)
