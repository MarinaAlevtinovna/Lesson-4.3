#Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f'Животное {self.name} поет')
    def eat(self):
        print(f'Животное {self.name} ест')

class Cat(Animal):
    def __init__(self, name, age, favorite_food):
        super().__init__(name, age)
        self.favorite_food = favorite_food

    def make_sound(self):
        print(f'{self.name} говорит "Мяу"')

    def eat(self):
        print(f'У {self.name} любимая еда {self.favorite_food}')


class Dog(Animal):
    def __init__(self, name, age, favorite_food):
        super().__init__(name, age)
        self.favorite_food = favorite_food

    def make_sound(self,):
        print(f'{self.name} говорит "Гав"')

    def eat(self):
        print(f'У {self.name} любимая еда {self.favorite_food}')

animals = [Cat('Кошка', '1', 'рыба'), Dog('Собака', '5', 'кость')]
for animal in animals:
    animal.make_sound()
    animal.eat()