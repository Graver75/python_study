from vprof import runner

n = 950

def non_recursive_factor(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


runner.run(non_recursive_factor, 'cmhp', args=[n], host='localhost', port=8000)