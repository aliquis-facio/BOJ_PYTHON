import sys
input = sys.stdin.readline


class Elem:
    def __init__(self, order, importance) -> None:
        self.order = order
        self.importance = importance


T = int(input())

for i in range(T):
    N, M = map(int, input().split())

    lst = list()
    importance_set = set()

    for importance, order in zip(map(int, input().split()), range(N)):
        lst.insert(0, Elem(order, importance))
        importance_set.add(importance)
