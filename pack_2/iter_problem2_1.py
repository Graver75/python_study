def non_recursive_factor(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print('Iterative factorial')
print('Your number is: ',non_recursive_factor(int(input("Enter number: "))))
