import sys
input = sys.stdin.readline

lst: list[int] = []
for i in range(5):
    lst.append(int(input().strip()))

lst.sort()

print(f"{int(sum(lst)/5)}\n{lst[2]}")
