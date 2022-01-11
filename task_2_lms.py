class Dog():
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self) -> int:
        return self.age * Dog.age_factor


tuzik = Dog(7)

if __name__ == '__main__':
    print(tuzik.human_age())
