def get_divisors(numb):
    arr = []
    for i in range(1, numb + 1):
        if numb % i == 0:
            arr.append(i)
    return arr


if __name__ == "__main__":
    print('Getting divisors')
    value = int(input('Enter number: '))
    print('Your result: ', get_divisors(value))
