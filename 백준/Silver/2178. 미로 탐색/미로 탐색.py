from collections import deque

N, M = map(int, input().split())
graph = []
for row in range(N):
    graph.append(list(map(int, input())))
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
q = deque()

def BFS(y, x):
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 1:
                    q.append((ny, nx))
                    graph[ny][nx] = graph[y][x] + 1
BFS(0, 0)
print(graph[N-1][M-1])