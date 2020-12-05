# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def person(**kwargs):
    return kwargs


name = input('Your name: ')
sur = input('Your surname: ')
year = int(input('Your year, wne you was born: '))
city = input('Your city: ')
email = input('Your email: ')
phone = input('Your phone number: ')
print(person(Name=name, Surname=sur, Year=year, City=city, Email=email, Phone_number=phone))