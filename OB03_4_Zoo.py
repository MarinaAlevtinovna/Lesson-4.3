#Используйте композицию для создания класса `Zoo`,
# который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

class Zoo:
    def __init__(self, zoo):
        self.zoo = zoo

class Human:
    def __init__(self, name_zoo):
        self.humans = {}
        self.zoo = Zoo(name_zoo)

    def add(self, name_human, position):
        self.humans[name_human] = position
        print(f'Вы добавили нового сотрудника {name_human}')

    def list(self):
        for name_human, position in self.humans.items():
            print(f'{name_human}: {position}')

class Animal:
    def __init__(self, name_zoo):
        self.animals = {}
        self.zoo = Zoo(name_zoo)

    def add(self, name_animal, quantity):
        self.animals[name_animal] = quantity
        print(f'Вы добавили новое животное {name_animal}')
    def list(self):
        for name_animal, quantity in self.animals.items():
            print(f'{name_animal}: {quantity}')


h = Human('Московский зоопарк')
h.add('Попов Антон', 'Охранник')
h.add('Сердюков Егор', 'Уборщик вальеров')


a = Animal('Московский зоопарк')
a.add('Пингвин', 5)
a.add('Крокодил', 2)

a.list()
h.list()

