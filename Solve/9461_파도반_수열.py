import sys
input = sys.stdin.readline


def P(num: int) -> int:
    global g_lst

    if g_lst[num]:
        return g_lst[num]

    g_lst[num] = 1 if num <= 3 else P(num - 2) + P(num - 3)
    return g_lst[num]


g_lst: list[int] = [0] * 101
T: int = int(input())
for _ in range(T):
    num: int = int(input())
    print(P(num))