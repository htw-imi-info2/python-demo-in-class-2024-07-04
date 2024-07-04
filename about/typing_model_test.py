
class A:
    def quack(self):
        return "quack a"


class B:
    def quack(self):
        return "quack b"


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
