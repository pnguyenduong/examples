'''
	Is-A, Has-A, Objects, and Classes
'''

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a class of Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name attribute
		self.name = name

## Cat is-a class of Animal
class Cat(Animal):

	def __init__(self,name):
		## Cat has-a name attribute
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name attribute
		self.name = name
		## Person has-a pet of some kind attribute
		self.pet = None

## Employee is-a class of Person
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## Employee has-a salary attribute
		self.salary = salary

##  Fish is-a object 
class Fish(object):
	pass

## Salmon is-a Class of Fish
class Salmon(Fish):
	pass

## Halibut is-a class of Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog('Rover')

## satan is-a Cat
satan = Cat('Satan')

## mary is-a Person
mary = Person('Mary')

# marry has-a pet
mary.pet = satan

## frank is-a Employee
frank = Employee('Frank', 120000)

## frank has-a pet
frank.pet = rover
## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()