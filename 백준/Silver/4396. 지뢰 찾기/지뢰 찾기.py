N = int(input())

mine = [list(map(str, input())) for _ in range(N)]
graph = [list(map(str, input())) for _ in range(N)]
rst = [['.' for _ in range(N)] for _ in range(N)]
flag = False

dy = [1, 0, -1, 0, 1, 1, -1, -1]
dx = [0, 1, 0, -1, 1, -1, 1, -1]

for i in range(N):
    for j in range(N):
        cnt = 0
        if graph[i][j] == 'x':
            if mine[i][j] == '*':
                flag = True
            for k in range(8):
                ny = i + dy[k]
                nx = j + dx[k]
                if 0 <= ny < N and 0 <= nx < N and mine[ny][nx] == '*':
                    cnt += 1
            rst[i][j] = cnt

if flag:
    for i in range(N):
        for j in range(N):
            if mine[i][j] == '*':
                print('*', end="")
            else:
                print(rst[i][j], end="")
        print()
        
else:
    for i in range(N):
        for j in range(N):
            print(rst[i][j], end="")
        print()