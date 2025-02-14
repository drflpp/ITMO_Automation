a: int = 5
b: str = 'stroka'
c: list = [1, 2]


def indent(s: str, width: int) ->str:
    return s, width

print(indent('dfr', 345))