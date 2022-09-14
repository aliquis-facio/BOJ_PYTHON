import sys
input = sys.stdin.readline

# 1 ≤ N ≤ 1,000,000
# 1 ≤ M ≤ 2,000,000,000
# 1 ≤ H ≤ 1,000,000,000

N, M = map(int, input().split())

trees = sorted(list(map(int, input().split())))

high = trees[N - 1]
low = trees[0]
if (high - low) <= M:
    low = 0

cnt = 0
while (low < high):
    mid = (high + low) // 2
    wood = 0

    for i in range(N - 1, 0, -1):
        if trees[i] > mid:
            wood += (trees[i] - mid)
        else:
            stopped_idx = i
            break

    if wood < M:
        high = mid
    else:
        low = mid + 1


print(low - 1)
