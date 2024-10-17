import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T: int = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x: int, y: int) -> bool:
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    
    if cabbage_farm[y][x] == 1:
        cabbage_farm[y][x] = 0
    
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        
        return True
    return False

for _ in range(T):
    M, N, K = map(int, input().split())

    cabbage_farm = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        cabbage_farm[y][x] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                cnt += 1
    
    print(cnt)