from hmac import digest_size
import sys
input = sys.stdin.readline


class IntDeque:
    def __init__(self) -> None:
        self.deque = list()
        self.dSize = 0

    def size(self):
        return self.dSize

    def empty(self):
        return 1 if self.dSize == 0 else 0

    def front(self):
        return self.deque[0] if self.empty() == 0 else -1

    def back(self):
        return self.deque[self.dSize - 1] if self.empty() == 0 else -1

    def push_front(self, x):
        self.dSize += 1
        self.deque.insert(0, x)
        # self.deque.append(x)

    def push_back(self, x):
        self.dSize += 1
        self.deque.append(x)
        # self.deque.insert(0, x)

    def pop_front(self):
        if self.empty() == 1:
            return -1
        else:
            self.dSize -= 1
            return self.deque.pop(0)

    def pop_back(self):
        if self.empty() == 1:
            return -1
        else:
            self.dSize -= 1
            return self.deque.pop(self.dSize)


N = int(input())

d = IntDeque()

for i in range(N):
    parse = input().split()

    if len(parse) == 1:
        print(getattr(d, parse[0])())
    else:
        getattr(d, parse[0])(int(parse[1]))
