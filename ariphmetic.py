def arithmetic(f, s, m):
    if m == "+":
        return f + s
    elif m == "*":
        return f * s
    elif m == "-":
        return f - s
    elif m == "/":
        return f / s
    else:
        return "Неизвестная операция"

print('Ariphmetic')
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
action = input('Enter action: ')
print('Your result: ', arithmetic(first, second, action))