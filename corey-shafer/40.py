class Employee:

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def full_name(self):
        return "{} {}".format(self.first, self.last)


emp_1 = Employee('Shuvam', 'Das', 60000)

print(Employee.full_name(emp_1))
print(emp_1.full_name())
