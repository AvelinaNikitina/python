# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self, speed):
        return speed

    def go(self):
        return f"{self.name}, {self.color} поехала"

    def stop(self):
        return f"{self.name}, {self.color} остановилась"

    def turn(self, direction):
        return f"Машина {self.name}, {self.color} повернула {direction}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Вы, {self.name}, {self.color}, превысили скорость!")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Вы, {self.name}, {self.color}, превысили скорость!")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(61, "black", "Mazda", True)
print(town_car.go())
town_car.show_speed()
print(town_car.turn("right"))
work_car = WorkCar(35, "blue", "Toyota", False)
print(town_car.go())
work_car.show_speed()
print(work_car.stop())
sport_car = SportCar(70, "red", "Mazda", True)
print(sport_car.go())
print(sport_car.turn("left"))
print(sport_car.stop())