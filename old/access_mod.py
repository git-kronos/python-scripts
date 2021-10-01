class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
    
    @property
    def Name(self):
        return self.__name 
    
    @Name.setter
    def Name(self, value):
        self.__name = value


if __name__=="__main__":
    p1 = Person("Tom", 12, "M")
    print(p1.Name)
    p1.Name("Jerry")
    
    print(p1.Name)
