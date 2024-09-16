N = int(input())
graph = [[' ' for _ in range(4*N)] for _ in range(4*N)]
coreX, coreY = 2 * (N-1), 2 * (N-1)
graph[coreY][coreX] = '*'
for i in range(1, N):
    for x in range(-2 * i, 2 * i + 1):
        graph[coreY - 2 * i][coreX + x] = '*'
        graph[coreY + 2 * i][coreX + x] = '*'
    for y in range(-2 * i, 2 * i + 1):
        graph[coreY + y][coreX - 2 * i] = '*'
        graph[coreY + y][coreX + 2 * i] = '*'

if N == 1:
    print(graph[0][0])
else:
    for x in range(0, 4 * (N-1) + 1):
        for y in range(0, 4 * (N-1) + 1):
            print(graph[x][y], end="")
        print()