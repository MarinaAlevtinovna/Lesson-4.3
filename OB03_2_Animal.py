#Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и
# переопределите методы, если требуется (например, различный звук для `make_sound()`).

class Animal():
    def way_move(self):
        print('Животные передвигаются')

class Bird(Animal):
    def __init__(self, move):
        self.move = move
    def way_move(self):
       print(f'Птицы {self.move}')

class Mammal(Animal):
    def __init__(self, move):
        self.move = move
    def way_move(self):
       print(f'Млекопитающие {self.move}')

class Reptile(Animal):
    def __init__(self, move):
        self.move = move
    def way_move(self):
       print(f'Рептилии {self.move}')

a = [Bird('летают'), Mammal('ходят'), Reptile('ползают')]
for animals in a:
    animals.way_move()