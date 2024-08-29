from basic.class_errors import Person
from math import factorial

person = Person('Santiago', 'Arteche', 25, 'Bra')
person.printPerson('Class called from module.py')
factorialFive = person.factorialPerson(5)
print(factorialFive)
print(factorial(5))