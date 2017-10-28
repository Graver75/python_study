import sys
sys.path.insert(0, '../pack_1')

from problem1_2 import get_divisors


def is_perfect(numb):
    return sum(get_divisors(numb)) - numb == numb

print('Checking for perfect')
try:
    print(is_perfect(int(input('Enter number: '))))
except Exception:
    print('Number should be natural!')
