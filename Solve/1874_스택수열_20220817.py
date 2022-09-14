import sys
input = sys.stdin.readline

n = int(input())

A = []
for i in range(n):
    A.append(int(input()))

B = []

num = 1
A_idx = 0
B_idx = -1

result = []

while (A_idx < n):
    if num <= A[A_idx]:
        B.append(num)
        B_idx += 1
        num += 1
        result.append('+')

    if B[B_idx] == A[A_idx]:
        B.pop()
        B_idx -= 1
        A_idx += 1
        result.append('-')
    elif B[B_idx] > A[A_idx]:
        print('NO')
        break
else:
    for ans in result:
        print(ans)
