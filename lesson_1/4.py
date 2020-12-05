num = int(input("Введите положительное число"))
if num>0:
    max = num % 10
    num = num // 10
    while num > 0:
        if num % 10 > max:
            max = num % 10
        num = num // 10
print (max)
