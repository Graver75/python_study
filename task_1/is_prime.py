def is_prime(numb):
    for i in range(2, numb - 1):
        if numb % i == 0:
            return False
    return True


print('Checking number for a prime')
value = int(input('Enter number: '))
print('Your number is', 'prime' if is_prime(value) else 'not prime')