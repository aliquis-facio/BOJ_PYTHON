import sys
input = sys.stdin.readline


class IntQueue:
    def __init__(self):
        self.q = list()
        self.qSize = 0

    def empty(self):
        return 1 if self.qSize == 0 else 0

    def size(self):
        return self.qSize

    def front(self):
        return self.q[0] if self.empty() == 0 else -1

    def back(self):
        return self.q[self.qSize - 1] if self.empty() == 0 else -1

    def pop(self):
        if self.empty() == 1:
            return -1
        else:
            self.qSize -= 1
            return self.q.pop(0)

    def push(self, x):
        self.qSize += 1
        self.q.append(x)


N = int(input())

intQueue = IntQueue()

for i in range(N):
    parse = input().split()
    if len(parse) == 1:
        print(getattr(intQueue, parse[0])())
    # 클래스 변수와 함수 이름이 같을 경우 getattr(obj, parse)로 실행 가능, getattr(obj, parse)()의 경우는 bound method error 발생
    else:
        getattr(intQueue, parse[0])(int(parse[1]))
