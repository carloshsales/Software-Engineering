from poo_basic.employee import Employee
from poo_basic.salary import Salary


age = 20
name = "Jupiter"
occupation = "Software Engeneer"
salary = Salary(3500, 250)
testEmployee = Employee(age, name, occupation, salary)


testEmployee.printTest()