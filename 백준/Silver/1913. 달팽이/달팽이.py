N = int(input())
target = int(input())
x, y = 0, 0
graph = [[0 for _ in range(N)] for _ in range(N)]

graph[N//2][N//2] = 1

for d in range(1, N//2 + 1):
    graph[N // 2 - d][N // 2 - d] = (2*d+1) * (2*d+1)
    graph[N // 2 + d][N // 2 - d] = graph[N // 2 - d][N // 2 - d] - 2 * d
    graph[N // 2 + d][N // 2 + d] = graph[N // 2 + d][N // 2 - d] - 2 * d
    graph[N // 2 - d][N // 2 + d] = graph[N // 2 + d][N // 2 + d] - 2 * d
    for i in range(1, 2*d):
        graph[N // 2 - d + i][N // 2 - d] = graph[N // 2 - d + i - 1][N // 2 - d] - 1
        graph[N // 2 + d][N // 2 - d + i] = graph[N // 2 + d][N // 2 - d + i - 1] - 1
        graph[N // 2 + d - i][N // 2 + d] = graph[N // 2 + d - i + 1][N // 2 + d] - 1
        graph[N // 2 - d][N // 2 + d - i] = graph[N // 2 - d][N // 2 + d - i + 1] - 1


for i in range(N):
    for j in range(N):
        if graph[i][j] == target:
            y, x = i+1, j+1
        print(graph[i][j], end=" ")
    print()
print(y, x)