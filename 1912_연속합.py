import sys
input = sys.stdin.readline

"""
5
-4 4 -3 3 6
5
1 2 3 -4 10
30
2 -3 10 -6 -2 -4 -5 3 -9 3 8 -6 -6 4 6 -7 5 -7 3 4 10 0 -3 -6 6 -9 -7 -10 0 -2
5
-1 0 -1 0 -1
10
10 -4 3 1 5 6 -35 12 21 -1
10
2 1 -4 3 4 -4 6 5 -5 1
5
-1 -2 -3 -4 -5
5
-1 2 1 1 1
5
-5 -4 -3 -2 -1

10
12
18
0
33
14
-1
5
-1
"""
def solve(n, lst):
    total_max = lst[0]
    # sub_sum = lst[0]
    sub_sum = 0

    for i in range(n):
        sub_sum += lst[i]

        # print(f"sub sum: {sub_sum}")
        if sub_sum > total_max:
            total_max = sub_sum
            # print(f"total: {total_max}")
        elif sub_sum <= 0:
            sub_sum = 0

        if total_max < 0 and total_max < lst[i]:
            total_max = lst[i]

    return total_max


while(True):
    n: int = int(input())
    if n == 0:
        break
    lst: list[int] = list(map(int, input().split()))

    print(f"ans: {solve(n, lst)}")
