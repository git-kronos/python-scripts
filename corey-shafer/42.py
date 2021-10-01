class Employee:

    no_of_emp = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.no_of_emp += 1

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)
        return self.pay

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp = Employee('Shuvam', 'Das', 60000)
emp_2 = Employee('Test', 'User', 50000)


# Employee.set_raise_amt(1.05)
# emp.set_raise_amt(1.20)

# new_emp_1 = Employee.from_string('John-Doe-70000')
# new_emp_2 = Employee.from_string('Jane-Doe-30000')
# new_emp_3 = Employee.from_string('Jack-Doe-90000')


# print(new_emp_1.email)
# print(new_emp_1.pay)

import datetime

my_date = datetime.date(2021, 10, 14)
print(my_date.weekday())
print(Employee.is_workday(my_date))
