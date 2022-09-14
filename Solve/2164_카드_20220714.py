import sys
from math import log2
input = sys.stdin.readline

N = int(input().strip())

k = log2(N)

if int(k) - k == 0:  # if k is R
    x = N
else:
    # x = 2 * ((2**int(k + 1) - 2**int(k)) - (2**int(k + 1) - N))
    x = 2 * (N - 2**int(k))

print(x)

# 1: 1
# 2: 2
# 3: 2 || 4: 4
# 5: 2 || 6: 4 || 7: 6 || 8: 8
# 9: 2 || 10: 4 || 11: 6 || 12: 8 || 13: 10 || 14: 12 || 15: 14 || 16: 16
