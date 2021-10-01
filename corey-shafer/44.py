class Employee:
    """
    A class for Employee Details
    """
    raise_ammount = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_ammount)
        return self.pay

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{}-{}'.format(self.full_name(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


if __name__ == "__main__":
    emp_1 = Employee('Shuvam', 'Das', 60000)
    emp_2 = Employee('Test', 'User', 50000)
    # print(emp_1.__repr__())
    # print(emp_1.__str__())

    # print(int.__add__(1, 2))
    # print(str.__add__('a', 'b'))
    # print(emp_1 + emp_2)
    print(len(emp_1))
    print(len(emp_2))
