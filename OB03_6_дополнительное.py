#Попробуйте добавить дополнительные функции в вашу программу,
# такие как сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

import json

class Zoo:
    def __init__(self, name):
        self.name = name

class Human:
    def __init__(self, name_zoo, humans_file='humans.txt'):
        self.humans = {}
        self.zoo = Zoo(name_zoo)
        self.humans_file = humans_file
        self.load_humans()

    def load_humans(self):
        try:
            with open(self.humans_file, 'r', encoding='utf-8') as file:
                for line in file:
                    name_human, position = line.strip().split(' - ')
                    self.humans[name_human] = position
        except FileNotFoundError:
            pass

    def save_humans(self):
        with open(self.humans_file, 'w', encoding='utf-8') as file:
            for name_human, position in self.humans.items():
                file.write(f'{name_human} - {position}\n')

    def add(self, name_human, position):
        self.humans[name_human] = position
        self.save_humans()
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
        try:
            with open(self.animals_file, 'r', encoding='utf-8') as file:
                for line in file:
                    name_animal, quantity = line.strip().split(' - ')
                    self.animals[name_animal] = int(quantity)
        except FileNotFoundError:
            pass

    def save_animals(self):
        with open(self.animals_file, 'w', encoding='utf-8') as file:
            for name_animal, quantity in self.animals.items():
                file.write(f'{name_animal} - {quantity}\n')

    def add(self, name_animal, quantity):
        self.animals[name_animal] = quantity
        self.save_animals()
        print(f'Вы добавили новое животное {name_animal}')

    def list(self):
        for name_animal, quantity in self.animals.items():
            print(f'{name_animal}: {quantity}')

class ZooManager:
    def __init__(self, zoo_name, humans_file='humans.txt', animals_file='animals.txt'):
        self.human_manager = Human(zoo_name, humans_file)
        self.animal_manager = Animal(zoo_name, animals_file)
        self.zoo_file = 'zoo_state.json'
        self.zoo = Zoo(zoo_name)
        self.load_zoo_state()

    def load_zoo_state(self):
        try:
            with open(self.zoo_file, 'r', encoding='utf-8') as file:
                state = json.load(file)
                self.human_manager.humans = state.get('humans', {})
                self.animal_manager.animals = state.get('animals', {})
        except FileNotFoundError:
            pass

    def save_zoo_state(self):
        state = {
            'humans': self.human_manager.humans,
            'animals': self.animal_manager.animals
        }
        with open(self.zoo_file, 'w', encoding='utf-8') as file:
            json.dump(state, file)

    def add_human(self, name_human, position):
        self.human_manager.add(name_human, position)
        self.save_zoo_state()

    def add_animal(self, name_animal, quantity):
        self.animal_manager.add(name_animal, quantity)
        self.save_zoo_state()

    def list_humans(self):
        self.human_manager.list()

    def list_animals(self):
        self.animal_manager.list()

zoo_manager = ZooManager('Московский зоопарк')
zoo_manager.add_human('Попов Антон', 'Охранник')
zoo_manager.add_human('Сердюков Егор', 'Уборщик вальеров')

zoo_manager.add_animal('Пингвин', 5)
zoo_manager.add_animal('Крокодил', 2)

print("Список животных:")
zoo_manager.list_animals()

print("Список сотрудников:")
zoo_manager.list_humans()