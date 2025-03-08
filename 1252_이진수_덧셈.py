import sys
from typing import *

input = sys.stdin.readline

a: str
b: str
a, b = map(str, input().split())
a = a[::-1]
b = b[::-1]
a_len: int = len(a)
b_len: int = len(b)
max_len: int = a_len if a_len > b_len else b_len
ans: List[str] = ['0'] * (max_len + 1)
check: int = 0
sum: int = 0

for i in range(max_len + 1):
    if i < a_len and i < b_len:
        sum = int(a[i]) + int(b[i]) + check
    elif i < a_len:
        sum = int(a[i]) + check
    elif i < b_len:
        sum = int(b[i]) + check
    else:
        sum = check
    
    match sum:
        case 3:
            check = 1
            ans[i] = '1'
        case 2:
            check = 1
            ans[i] = '0'
        case 1:
            check = 0
            ans[i] = '1'
        case 0:
            check = 0
            ans[i] = '0'

if ans[0] == '0':
    print(''.join(ans[::-1]))
else:
    print(''.join(ans[max_len - 1::-1]))