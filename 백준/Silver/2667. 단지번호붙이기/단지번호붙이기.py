N = int(input())
graph = []
for row in range(N):
    graph.append(list(map(int, input())))
isVisited = [[0 for _ in range(N)] for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
cnt = 0
rst = []
def DFS(y, x):
    if isVisited[y][x] == 0:
        isVisited[y][x] = 1
        global cnt
        cnt += 1
        for i in range(4):
            if 0 <= y+dy[i] < N and 0<= x+dx[i] < N:
                if isVisited[y+dy[i]][x+dx[i]] == 0 and graph[y+dy[i]][x+dx[i]] == 1:
                    DFS(y+dy[i], x+dx[i])



for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and isVisited[i][j] == 0:
            cnt = 0
            DFS(i, j)
            rst.append(cnt)

rst.sort()
print(len(rst))
for num in rst:
    print(num)