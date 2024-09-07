from collections import deque

M, N = map(int, input().split())
graph = []
sum = 0
rst = 0
max = -100
tomato = []
isVisited = [[-1 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, input().split())))


def BFS(tomatoList):
    q = deque()
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    for y, x in tomatoList:
        q.append((y, x))
        isVisited[y][x] = 0
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0<=ny<N and 0<=nx<M:
                if isVisited[ny][nx] == -1 and graph[ny][nx] == 0:
                    isVisited[ny][nx] = isVisited[cy][cx] + 1
                    q.append((ny, nx))


for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            sum += 1
        elif graph[i][j] == 1:
            tomato.append((i, j))
            sum += 1

BFS(tomato)

for i in range(N):
    for j in range(M):
        if isVisited[i][j] != -1:
            rst += 1
        if isVisited[i][j] >= max:
            max = isVisited[i][j]


if sum == rst:
    print(max)
else:
    print(-1)
