#Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Zoo:
    def __init__(self, zoo):
        self.zoo = zoo

class ZooKeeper:
    def __init__(self, zoo_name):
        self.zoo = Zoo(zoo_name)
        self.feed_animals = {}

    def feed_animal(self, name_animal, time):
        self.feed_animals[name_animal] = time
        print(f'Покормить {name_animal} в {time}')


class Veterinarian:
    def __init__(self, zoo_name):
        self.zoo = Zoo(zoo_name)
        self.heal_animals = {}

    def heal_animal(self, name_animal, disease):
        self.heal_animals[name_animal] = disease
        print(f'{name_animal} - {disease}')

zk = ZooKeeper('Калининградский зоопарк')
zk.feed_animal('Крокодил', 10.00)
zk.feed_animal('Обезьяны', 13.00)

v = Veterinarian('Калининградский зоопарк')
v.heal_animal('Слон', 'Депрессия')
v.heal_animal('Динозавр', 'Вымирание')