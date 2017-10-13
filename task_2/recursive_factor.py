from vprof import runner
import sys
sys.setrecursionlimit(2500)

n = 950


def recursive_factor(n):
    if n == 1:
        return 1
    return n * recursive_factor(n - 1)


runner.run(recursive_factor, 'cmhp', args=[n], host='localhost', port=8000)
