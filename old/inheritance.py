"""
Inheritance
"""

class Pet:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name}, and I am {self.age} years old")
    
    def speak(self):
        print("I dont know what I say")


class Cat(Pet):
    def __init__(self, name, age, color) -> None:
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name}, and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass



if __name__ == "__main__":
    d = Dog("Bob", 7)
    d.show()
    d.speak()

    c = Cat("Tom", 6, 'Brown')
    c.show()
    c.speak()

    f = Fish("Neo", 5)
    f.speak()
    f.show()