import sys
from typing import *

input = sys.stdin.readline

N:int = int(input())
numbers:List[int] = list(map(int, input().split()))
stack:List[int] = []
p:int = 1

for n in numbers:
    if n == p:
        p += 1
        continue
    else:
        while(stack):
            if stack[-1] == p:
                stack.pop()
                p += 1
            else:
                break
        
        stack.append(n)

while(stack):
    if stack[-1] == p:
        stack.pop()
        p += 1
    else:
        break

if stack:
    print("Sad")
else:
    print("Nice")