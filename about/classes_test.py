import pytest


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age >= 0:
            self.age = age
        else:
            raise ValueError("Age cannot be negative")

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

def test_person():
# Example usage:
    person = Person("John Doe", 30)
    assert str(person) == "Person(name=John Doe, age=30)"  # Output: Person(name=John Doe, age=30)

    # print(person.get_name())  # Output: John Doe
    # person.set_name("Jane Doe")
    # print(person)  # Output: Person(name=Jane Doe, age=30)
    #
    # print(person.get_age())  # Output: 30
    # person.set_age(25)
    # print(person)  # Output: Person(name=Jane Doe, age=25)

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
