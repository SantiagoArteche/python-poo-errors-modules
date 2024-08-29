class Person:
    def __init__(self, name, surname, age, country = 'Arg') -> None:
        self.__name = name
        self.__surname = surname
        self.age = age
        self.country = country
    def printPerson(self, newParameter = 'SelfAssigned'):
        print(f"First name: {self.__name} \nSurname: {self.__surname} \nAge: {self.age}\n{self.country}\n{newParameter}")

    def factorialPerson(self, n):
        if(n == 0): 
            return 1
        
        return n * self.factorialPerson(n - 1)

person1 = Person('Santiago', 'Arteche', 25)
person1.newProperty = 'This is a new property'
person1.printPerson('Man')

my_tuple = tuple([1,2,3,4,5,6])
try:
    my_tuple[0] = 0
    print(my_tuple)
except ValueError as error:
    print(error)
except Exception as exception:
    print(f"ERROR: {exception}")
else:
    print('Continue the ejecution')
finally:
    print('Program finished')