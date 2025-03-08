import sys
from typing import Dict, List

input = sys.stdin.readline

N: int # 2 <= N 2 <= 200
M: int # 1 <= M <= N^2
P: int # 1 <= P <= 100,000
x: int # 1 <= x <= N
y: int # 1 <= y <= N
t: int # 1 <= t <= 100
path: str # N: North, E: East, W: West, S: South
direction: Dict[chr, List[int, int]] = {'N': [0, 1], 'E': [1, 0], 'W': [-1, 0], 'S':[0, -1]}
board: List[List] = []