class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'My name is {self.name}'

    def say_hi(self):
        ...


class Student(Person):
    def __init__(self, name: str, age: int, college: str, specialization: str, course: int):
        super().__init__(name, age)
        self.college = college
        self.specialization = specialization
        self.course = course

    def __str__(self):
        return f"My name is {self.name} and I'm a student"

    def say_hi(self):
        print(
            f"Hi, may name is {self.name}, I'm a student at {self.college}. I study {self.specialization}")


class Teacher(Person):
    def __init__(self, name, age, college, specialization, salary):
        super().__init__(name, age)
        self.college = college
        self.specialization = specialization
        self.salary = salary

    def __str__(self):
        return f"My name is {self.name} and I'm a teacher"

    def say_hi(self):
        print(f"Hi, may name is {self.name}, I'm a teacher at {self.college}. I teach {self.specialization}")


def main():
    bob = Student(name='Bob Brown', age=21, college='First college', specialization='Law', course=3)
    mary = Teacher(name='Mary Jaine', age=45, college='First college', specialization='Law', salary='2000$')
    bob.say_hi()
    mary.say_hi()
    print(bob)
    print(mary)


if __name__ == '__main__':
    main()
