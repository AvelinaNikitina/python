# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def my_math(param_1, param_2):
    if param_2 == 0:
        print(f"Невозможно подилить число на ноль.")
    else:
        return param_1 / param_2


с = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(my_math(с, b))
