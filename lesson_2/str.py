#Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
#Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
line = input("Введите строку из нескольких слов: ")
word=[]
number = 1
for k in range(line.count(" ") + 1):
    word= line.split()
    if len(str(word)) <= 10:
        print(f" {number} {word [k]}")
        number += 1
    else:
        print(f" {number} {word[k][0:10]}")
        number += 1
