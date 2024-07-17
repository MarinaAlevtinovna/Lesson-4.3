#Попробуйте добавить дополнительные функции в вашу программу,
# такие как сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

class Zoo:
    def __init__(self, zoo):
        self.zoo = zoo

class Human:
    def __init__(self, name_zoo, humans_file='humans.txt'):
        self.humans = {}
        self.zoo = Zoo(name_zoo)
        self.humans_file = humans_file
        self.load_humans()

    def load_humans(self):
        with open(self.humans_file, 'r', encoding='utf-8') as file:
            for line in file:
                name_human, position = line.strip().split(' - ')
                self.humans[name_human] = position

    def add(self, name_human, position):
        self.humans[name_human] = position
        with open(self.humans_file, 'a', encoding='utf-8') as file:
            file.write(f'{name_human} - {position}\n')
        print(f'Вы добавили нового сотрудника {name_human} - {position}')

    def list(self):
        for name_human, position in self.humans.items():
            print(f'{name_human}: {position}')

class Animal:
    def __init__(self, name_zoo, animals_file='animals.txt'):
        self.animals = {}
        self.zoo = Zoo(name_zoo)
        self.animals_file = animals_file
        self.load_animals()

    def load_animals(self):
        with open(self.animals_file, 'r', encoding='utf-8') as file:
            for line in file:
                name_animal, quantity = line.strip().split(' - ')
                self.animals[name_animal] = int(quantity)

    def add(self, name_animal, quantity):
        self.animals[name_animal] = quantity
        with open(self.animals_file, 'a', encoding='utf-8') as file:
            file.write(f'{name_animal} - {quantity}\n')
        print(f'Вы добавили новое животное {name_animal}')

    def list(self):
        for name_animal, quantity in self.animals.items():
            print(f'{name_animal}: {quantity}')

# Пример использования:
h = Human('Московский зоопарк')
h.add('Попов Антон', 'Охранник')
h.add('Сердюков Егор', 'Уборщик вальеров')

a = Animal('Московский зоопарк')
a.add('Пингвин', 5)
a.add('Крокодил', 2)

print("Список животных:")
a.list()

print("Список сотрудников:")
h.list()