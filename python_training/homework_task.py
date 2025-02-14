def giving_back(a=(1, 2, 3, 4)):
    return a[1]


print(giving_back((2, 3)))


def back_2(radius, pi=3.14159):
    s = pi*radius**2
    return s


print(back_2(2))


def length(s: str = '') -> float:
    return len(s)

print(length('fghoo'))


def length_list(a: list, b: list) -> int:
    return max(len(a), len(b))

print(length_list([1,2,3,4], [3, 4]))


def cont(l: list):
    l.append(3)
    return l


def summa(l:list) -> float:
    return sum(l)