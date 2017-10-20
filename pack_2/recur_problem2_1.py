import sys
sys.setrecursionlimit(2500)

def recursive_factor(n):
    if n == 1:
        return 1
    return n * recursive_factor(n - 1)

print("Recursive factor")
print("Your number is: ", recursive_factor(int(input('Enter your number: '))))
