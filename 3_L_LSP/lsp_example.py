class Animal:
    def comer(self):
        print('O animal esta comendo')

    def andar(self):
        print('O animal esta andando na jaula')


class Felino(Animal):
    def lamber(self):
        print('O Felino esta lambendo seu pelo')


class Leao(Felino):
    def rugir(self):
        print('O leao esta rugindo alto!!!')


class Pessoa:
    def observa(self, animal: Animal):
        animal.comer()


renatinho = Pessoa()
animal = Animal()
felino = Felino()

animal.comer()
felino.comer()

renatinho.observa(animal)
