class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self) -> None:
        print(f'Hello, my name is {self.first_name} {self.last_name} and I\'m {self.age} years old.')


polina = Person('Polina', 'Goncharenko', 24)
carl = Person('Carl', 'Johnson', 26)

if __name__ == '__main__':
    polina.talk()
    carl.talk()
