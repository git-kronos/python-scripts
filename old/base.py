class Dog:
    def __init__(self, *args, **kwargs) -> None:
        self.name = kwargs.get('name')
        self.age = kwargs.get('age')

    def get_name(self):
        return self.name
    
    def set_name(self, name: str):
        self.name = name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age: int):
        self.age = age


if __name__ == "__main__":
    d = Dog(name='moti', age=6)
    e = Dog(name='x', age=6)

    print(d.get_name())
    print(d.get_age())

    print(e.get_name())
    print(e.get_age())
