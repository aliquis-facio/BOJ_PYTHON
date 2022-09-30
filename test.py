from inspect import stack
import sys
input = sys.stdin.readline

left = []
center = [0]
right = [0]
prev = 0


def solve(n, l, c, r):
    global left, center, right, prev
    if (n > 0):
        solve(n - 1, l, r, c)
        r.append(l.pop())
        print(r[-1])
        solve(n - 1, c, l, r)


T = int(input())

for i in range(T):
    n = int(input())

    left = [i for i in range(n + 1)]
    solve(n, left, center, right)
