import sys
from typing import *

input = sys.stdin.readline

n: int = int(input().strip())
lst: List[int] = list(map(int, input().split()))

curr_max: int = lst[0] # 최댓값
prefix_sum: int = lst[0] # 누적합
check: bool = True

for i in range(1, n): # 1 ~ n-1까지 반복
    if check:
        prefix_sum += lst[i] # 누적합 계산
    else:
        check = True

    if prefix_sum > curr_max: # 누적합값이 최댓값보다 클 경우
        curr_max = prefix_sum

    if lst[i] > curr_max: # lst[i]가 최댓값보다 클 경우
        curr_max = lst[i]
        prefix_sum = lst[i] # lst[i]가 누적합값보다 큼
    
    if prefix_sum < 0:
        if i + 1 < n: # IOE 방지
            prefix_sum = lst[i + 1] # 누적합값을 lst[i + 1] 값으로 초기화
            check = False # 다음 누적합 계산 생략 -> 중복값 계산 X

print(curr_max)