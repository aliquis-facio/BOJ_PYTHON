import statistics
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

mat = []
arr = []

for i in range(N):
    temp = input().split()
    mat.append(temp)
    arr += temp

# for row in mat:
#     for elem in row:
#         arr.append(elem)

print(arr)

modeNum = statistics.mode(arr)
print(modeNum)
