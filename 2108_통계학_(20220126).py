import sys
input = sys.stdin.readline


def solution1():
    import statistics

    N = int(input().strip())

    num_lst = []

    for i in range(N):
        num = int(input().strip())
        num_lst.append(num)

    num_lst.sort()

    arithmetic_mean = round(statistics.mean(num_lst))
    median_num = statistics.median(num_lst)
    mode_num_lst = statistics.multimode(num_lst)
    num_range = num_lst[-1] - num_lst[0]

    print(arithmetic_mean)
    print(median_num)
    if len(mode_num_lst) > 1:
        print(mode_num_lst[1])
    else:
        print(mode_num_lst[0])
    print(num_range)


N = int(input())

lst = int(input().split())

mean = round(sum(lst)/N, 0)
center =
