class Employee:
    no_of_emp = 0
    raise_ammount = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.no_of_emp += 1

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_ammount)
        return self.pay


emp = Employee('Shuvam', 'Das', 60000)
emp_2 = Employee('Test', 'User', 50000)

emp.raise_ammount = 1.05
print(Employee.__dict__)
print()
print(Employee.no_of_emp)
print()
print(emp.__dict__)
print(Employee.raise_ammount)
print(emp.raise_ammount)
print(emp_2.raise_ammount)
