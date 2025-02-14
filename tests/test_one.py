def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

#
# def test_fail():
#     assert 'test' == 'testing'

# Функция для проверки на несоответсвие
def test_not():
    a  = 'test'
    b = 'testing'
    assert not a == b

def test_list():
    x = ['a', 'b', 'c']
    y = [1, 2, 3]
    assert not x == y
    assert x != y
a = 3
b = 5
c = 7
def test_numbers(a, b, c):
    assert a.is_integer()
    assert b.is_integer()
    assert c.is_integer()

def test_triangle(a, b, c):
    l = [a, b, c]
    assert sorted(l)[0] + sorted(l)[1] > sorted(l)[2]

def test_right(a, b, c):
