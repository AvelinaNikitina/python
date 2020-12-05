password=[]
symbol = 0
while symbol != "*":
    symbol = input("Введите символ, из которого должен быть пароль. Чтобы завершить ввод, напишите *: ")
    password.append(symbol)
password.pop(len(password) - 1)
if len(password) // 2 == 0:
    for first in range(0, len(password), 2):
        password[first], password[first + 1] = password[first+1], password[first]
else:
    for first in range(0, (len(password) - 1), 2):
        password[first], password[first + 1] = password[first+1], password[first]
print(password)