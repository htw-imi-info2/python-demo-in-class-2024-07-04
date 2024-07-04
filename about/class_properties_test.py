import pytest

#https://docs.python.org/3/library/functions.html#property
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age
        else:
            raise ValueError("Age cannot be negative")

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

def test_person():
# Example usage:
    person = Person("John Doe", 30)
    assert str(person) == "Person(name=John Doe, age=30)"  # Output: Person(name=John Doe, age=30)

def test_properties():
    person = Person("John Doe", 30)
    assert person.name == "John Doe"
    # print(person.get_name())  # Output: John Doe
    person.name = "Jane Doe"
    assert person.name == "Jane Doe"
    # print(person)  # Output: Person(name=Jane Doe, age=30)
    #
    # print(person.get_age())  # Output: 30
    assert person.age == 30
    person.age = 25
    assert person.age == 25
    # print(person)  # Output: Person(name=Jane Doe, age=25)

def test_properties_02():
    person = Person("John Doe", 30)
    assert 'age' in dir(person)
    assert 'name' in dir(person)
def test_return_value_without_return():
    person = Person("John Doe", 30)
    assert person.set_name("Max Mustermensch") == None


def test_methods_are_object_members():
    person = Person("John Doe", 30)

    assert person.get_name() == 'John Doe'
    def new_name():
        return "Alice"

    person.get_name = new_name

    assert person.get_name() == 'Alice'


def test_methods_are_object_members_02():
    a_list = [1, 4, 9, 16, 25]
    method_reference = a_list.reverse
    assert [1, 4, 9, 16, 25] == a_list

    method_reference()
    assert [25, 16, 9, 4, 1] == a_list, "after reverse"

    assert  str(a_list.reverse).startswith('<built-in method reverse of list object at ')
