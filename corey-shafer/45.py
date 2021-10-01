class Employee:
    """
    A class for Employee Details
    """

    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@company.com'

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Name Deleted')
        self.first = None
        self.last = None


if __name__ == "__main__":
    emp = Employee('Shuvam', 'Das')

    emp.fullname = "Test User"
    del emp.fullname
    print(emp.first)
    print(emp.last)
    print(emp.email)
    print(emp.fullname)
