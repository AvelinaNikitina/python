'''
 Реализовать функцию my_func(),
 которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
'''


def my_func(numbers):
    max_ = max(numbers)
    a = numbers.index(max_)
    numbers.pop(a)
    max_1 = max(numbers)
    return max_ + max_1


numbers = []
for i in range (3):
    a = int(input("Please, give me the first argument: "))
    numbers.append(a)
print(my_func(numbers))