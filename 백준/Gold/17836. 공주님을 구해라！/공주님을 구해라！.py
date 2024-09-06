import sys
from collections import deque
MAX = 20000
N, M, T = map(int, input().split())
graph = []
swy, swx = 0, 0
isVisited = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 2:
            swy, swx = i, j

def BFS(sy, sx, ey, ex):
    isVisited = [[0 for _ in range(M)] for _ in range(N)]
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    cnt = 0
    q = deque()
    q.append((sy, sx))
    isVisited[sy][sx] = 1
    while q:
        cy, cx = q.popleft()
        if cy == ey and cx == ex:
            return int(isVisited[cy][cx])
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= nx < M and 0 <= ny < N:
                if isVisited[ny][nx] == 0 and graph[ny][nx] != 1:
                    q.append((ny, nx))
                    isVisited[ny][nx] = isVisited[cy][cx] + 1
        cnt += 1
    return MAX


noSword = BFS(0, 0, N-1, M-1) - 1
withSword = BFS(0, 0, swy, swx) + (N-1 - swy) + (M-1 - swx) - 1

rst = min(noSword, withSword)
if rst > T:
    print("Fail")
else:
    print(rst)