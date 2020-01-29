#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     05/02/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Employee:
    ''' This is help documentation.
    '''
    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print Employee.raise_amount
#Employee.raise_amount = 1.05
print Employee.raise_amount
emp_1.raise_amount = 1.05
print emp_1.raise_amount
print emp_2.raise_amount  # accesses class value.

emp_1.raise_amount = 1.05

print (emp_1.__dict__)

print Employee.num_of_emp

