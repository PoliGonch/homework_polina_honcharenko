class Animal:

    def talk(self):
        ...


class Dog(Animal):

    def talk(self):
        print('Woof woof')


class Cat(Animal):

    def talk(self):
        print('Meow')


def animal_talk(animal):
    animal.talk()


pushok = Cat()
tuzik = Dog()
animal_talk(tuzik)
