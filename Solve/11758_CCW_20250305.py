from sys import stdin
from typing import *

input = stdin.readline

P1: List[int] = list(map(int, input().split())) # [x1, y1]
P2: List[int] = list(map(int, input().split())) # [x2, y2]
P3: List[int] = list(map(int, input().split())) # [x3, y3]

point: int = (P2[1] - P1[1]) * (P3[0] - P1[0]) + (P2[0] - P1[0]) * P1[1]

direct: int
if point > (P2[0] - P1[0]) * P3[1]:
    direct = -1
elif point == (P2[0] - P1[0]) * P3[1]:
    direct = 0
else:
    direct = 1

print(direct)