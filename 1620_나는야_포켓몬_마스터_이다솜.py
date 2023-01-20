import sys
input = sys.stdin.readline

N, M = map(int, input().split())

map = dict()
for i in range(N):
    map.setdefault(i + 1, input().strip())

for i in range(M):
    string = input().strip()
    if string.isalpha():
        print("ans: ", end="")
        print(map.get(string))
    else:
        print("ans: ", end="")
        print(map[int(string)])
