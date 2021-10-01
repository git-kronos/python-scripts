"""
class attribute
class method
static method
"""

class Person:
    number_of_people = 0
    
    def __init__(self, name) -> None:
        self.name = name
        Person.number_of_people += 1
        Person.add_person()
    
    @classmethod
    def add_person(cls):
        cls.number_of_people + 1

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    

class Math:    
    @staticmethod
    def adds(x):
        return x + 5



if __name__=="__main__":
    p1 = Person("Tom")
    p2 = Person("Bob")
    p3 = Person("Jerry")

    print(Person.number_of_people_())
    print(Math.adds(5))
