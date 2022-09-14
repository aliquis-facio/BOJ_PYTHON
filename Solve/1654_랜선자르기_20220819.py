import sys
input = sys.stdin.readline

K, N = map(int, input().split())

high = 1
lst = []

for i in range(K):
    val = int(input())

    if val > high:
        high = val

    lst.append(val)

high += 1
low = 0

while (low < high):
    mid = (high + low) // 2

    cnt = 0

    for i in range(K):
        cnt += (lst[i] // mid)

    if (cnt < N):
        high = mid
    else:
        low = mid + 1

print(low - 1)
