import sys

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

R, C, N = map(int, input().split())

base = []
graph = [[0 for _ in range(C)] for _ in range(R)]
blow = []

for row in range(R):
    base.append(list(map(str, input())))


for row in range(R):
    for col in range(C):
        if base[row][col] == 'O':
            graph[row][col] = 3
        else:
            graph[row][col] = 0

if N == 1:
    for row in range(R):
        for col in range(C):
            print(base[row][col], end="")
        print()
    sys.exit()

for i in range(2, N+1):
    blow = []
    if i % 2 == 0:
        for row in range(R):
            for col in range(C):
                if graph[row][col] == 0:
                    graph[row][col] = i+3
    else:
        for row in range(R):
            for col in range(C):
                if i == graph[row][col]:
                    blow.append((row, col))
                    for dir in range(4):
                        nextY = row + dy[dir]
                        nextX = col + dx[dir]
                        if 0 <= nextY < R and 0 <= nextX < C:
                            blow.append((row+dy[dir], col+dx[dir]))
        list(set(blow))
        for j in blow:
            graph[j[0]][j[1]] = 0

for row in range(R):
    for col in range(C):
        if graph[row][col] == 0:
            graph[row][col] = '.'
        else:
            graph[row][col] = 'O'

for row in range(R):
    for col in range(C):
        print(graph[row][col], end="")
    print()



