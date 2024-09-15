qwerty = {'q': (0, 0, 0), 'w': (0, 1, 0), 'e': (0, 2, 0), 'r': (0, 3, 0), 't': (0, 4, 0),
          'y': (0, 5, 1), 'u': (0, 6, 1), 'i': (0, 7, 1), 'o': (0, 8, 1), 'p': (0, 9, 1),
          'a': (1, 0, 0), 's': (1, 1, 0), 'd': (1, 2, 0), 'f': (1, 3, 0), 'g': (1, 4, 0),
          'h': (1, 5, 1), 'j': (1, 6, 1), 'k': (1, 7, 1), 'l': (1, 8, 1),
          'z': (2, 0, 0), 'x': (2, 1, 0), 'c': (2, 2, 0), 'v': (2, 3, 0), 'b': (2, 4, 1), 'n': (2, 5, 1), 'm': (2, 6, 1)}

L, R = input().split()
line = input()
cnt = 0

ly, lx = qwerty[L][0], qwerty[L][1]
ry, rx = qwerty[R][0], qwerty[R][1]

for alpha in line:
    ny, nx, lr = qwerty[alpha][0], qwerty[alpha][1], qwerty[alpha][2]
    if lr == 0:
        cy, cx = ly, lx
        ly, lx = ny, nx
    else:
        cy, cx = ry, rx
        ry, rx = ny, nx
    cnt += (abs(cy - ny) + abs(cx - nx))
    cnt += 1


print(cnt)