all_sec = int(input("Введите время в секундах"))
hours = all_sec // 3600
minutes = (all_sec % 3600) // 60
seconds = all_sec % 60
print(hours, ":", minutes, ":", seconds)