from collections import deque

M, N, H = map(int, input().split())
graph = []
sum = 0
rst = 0
max = -100
tomato = []
isVisited = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]

for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int, input().split())))
    graph.append(tmp)


def BFS(tomatoList):
    q = deque()
    dy = [1, 0, -1, 0, 0, 0]
    dx = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    for z, y, x in tomatoList:
        q.append((z, y, x))
        isVisited[z][y][x] = 0
    while q:
        cz, cy, cx = q.popleft()
        for i in range(6):
            nz, ny, nx = cz + dz[i], cy + dy[i], cx + dx[i]
            if 0<=nz<H and 0<=ny<N and 0<=nx<M:
                if isVisited[nz][ny][nx] == -1 and graph[nz][ny][nx] == 0:
                    isVisited[nz][ny][nx] = isVisited[cz][cy][cx] + 1
                    q.append((nz, ny, nx))

for k in range(H):
    for i in range(N):
        for j in range(M):
            if graph[k][i][j] == 0:
                sum += 1
            elif graph[k][i][j] == 1:
                tomato.append((k, i, j))
                sum += 1

BFS(tomato)

for k in range(H):
    for i in range(N):
        for j in range(M):
            if isVisited[k][i][j] != -1:
                rst += 1
            if isVisited[k][i][j] >= max:
                max = isVisited[k][i][j]


if sum == rst:
    print(max)
else:
    print(-1)
