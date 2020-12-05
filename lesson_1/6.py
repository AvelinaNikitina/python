res = float(input("Введите результат спортсмена в первый день"))
max = float(input("Введите результат, к которому стремится спортсмен"))
day = 1
print(day, "день:", res, "км")
while max - res >= 0:
        day += 1
        res = res + res * 0.1
        res = round(res, 2)
        print(day, "день:", res, "км")
