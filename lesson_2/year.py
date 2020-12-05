year = ["winter","sprint","summer","autumn"]
month = int(input("Введите число месяцв: "))
if (month < 0) or (month > 12):
    month = input("Вы ввели некоректное число, попробуйте еще раз: ")
else:
    if (month == 12) or (month < 3):
        print("Это зима")
    elif (month > 2) and (month < 6):
        print("Это весна")
    elif (month > 5) and (month < 9):
        print("Это лето")
    elif (month > 8) and (month < 12):
        print("Это осень")
