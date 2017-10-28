from iter_problem2_1 import non_recursive_factor as factor


def get_binomial_coeff(n, k):
    return factor(n) // (factor(k) * factor(n-k))


def print_pascal_triangle(n):
    k = 0
    for i in range(n + 1):
        i = 0
        print(' ' * (n - k), end='')
        while i <= k:
            print(get_binomial_coeff(k, i), end=" ")
            i += 1
        print(end='\n')
        k += 1

print('Pascal triangle')
try:
    print_pascal_triangle(int(input('Enter number: ')))
except Exception:
    print('Number should be natural!')