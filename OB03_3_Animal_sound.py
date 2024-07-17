#Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

class Animal():
    def make_sound(self):
        return 'Животное разговаривает'

class Cat():
    def make_sound(self):
        return 'Кошка говорит "Мяу"'
class Dog():
    def make_sound(self):
        return 'Собака говорит "Гав"'

def animal_sound(animal):
    print(animal.make_sound())

cat = Cat()
dog = Dog()

animal_sound(cat)
animal_sound(dog)

