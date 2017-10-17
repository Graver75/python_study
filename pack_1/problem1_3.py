from problem1_2 import get_divisors


def is_prime(numb):
    return len(get_divisors(numb)) < 3


print('Checking number for a prime')
value = int(input('Enter number: '))
print('Your number is', 'prime' if is_prime(value) else 'not prime')