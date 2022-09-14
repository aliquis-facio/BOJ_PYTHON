import sys
input = sys.stdin.readline


class Node(object):
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


class DLList(object):
    def __init__(self) -> None:
        self.head = Node()
        self.head.right = self.head
        self.size = 0

    def isEmpty(self):
        return self.head.right == self.head

    def append(self, data):
        insert = Node(data)

        if self.isEmpty():
            self.head.right = insert
            insert.left = insert.right = insert
        else:
            pos = self.head.right.left
            insert.left = pos
            pos.right.left = insert
            insert.right = pos.right
            pos.right = insert

        self.size += 1

        return insert

    def print3(self, K):
        pos = self.head.right

        cnt = 1
        print('<', end='')
        while(self.size > 1):
            if cnt % K == 0:
                pos.left.right = pos.right
                pos.right.left = pos.left
                self.size -= 1
                print(pos.data, end=', ')

            cnt += 1
            pos = pos.right
        print(pos.data, end='>')


N, K = map(int, input().split())

lst = DLList()

for n in range(1, N + 1):
    lst.append(n)

lst.print3(K)
