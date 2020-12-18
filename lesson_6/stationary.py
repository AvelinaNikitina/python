#  Реализовать класс Stationery (канцелярская принадлежность).
#  Определить в нем атрибут title (название) и метод draw (отрисовка).
#  Метод выводит сообщение “Запуск отрисовки.”
#  Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
#  В каждом из классов реализовать переопределение метода draw.
#  Для каждого из классов методы должен выводить уникальное сообщение.
#  Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки"


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'


pen = Pen("ручка")
print(pen.draw())
pencil = Pencil("карандаш")
print(pencil.draw())
handle = Handle("маркер")
print(handle.draw())
