import random

import Base

l = Base.PositionalList()

n = int(input('Amount of requests: '))

i = 0
while l.len() < n:
    probability = random.randint(0, 1)
    if probability:
        l.add_last(i)
    probability = random.randint(0, 100)
    if probability > 20:
        i += 1

for i in l:
    print(i, end=' ')
print()

v = int(input('Guess sum: '))


def search():
    global l, v
    a = l._header._next
    b = l._trailer._prev

    while a != b:
        if a._element + b._element == v:
            return a._element, b._element
        elif a._element + b._element < v:
            a = a._next
        else:
            b = b._prev
    return None

print(search())