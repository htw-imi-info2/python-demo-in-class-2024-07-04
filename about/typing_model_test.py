
class A:
    def quack(self):
        return "quack a"


class B:
    def quack(self):
        return "quack b"


# Duck Type: If it quacks like a duck...
# https://en.wikipedia.org/wiki/Duck_test
# (type is not defined, but there's an
# implicit type that quacks -
# so probably a duck
# -> Dynamic Typing

def method_wants_a_duck(duck):
    return duck.quack()


def test_is_it_a_duck():
    a = A()
    b = B()
    assert a.quack() == 'quack a'
    assert b.quack() == 'quack b'


def test_is_it_a_duck_with_method():
    a = A()
    b = B()
    assert method_wants_a_duck(a) == 'quack a'
    assert method_wants_a_duck(b) == 'quack b'
