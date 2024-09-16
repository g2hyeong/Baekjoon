line = list(input())
stack = []
flag = False
for i in range(len(line)):
    if line[i] == '<':
        while len(stack) != 0:
            print(stack.pop(), end="")
        flag = True

    if flag:
        print(line[i], end="")
    else:
        if line[i] == ' ':
            while len(stack) != 0:
                print(stack.pop(), end="")
            print(line[i], end="")
        else:
            stack.append(line[i])

    if line[i] == '>':
        flag = False

while len(stack) != 0:
    print(stack.pop(), end="")
