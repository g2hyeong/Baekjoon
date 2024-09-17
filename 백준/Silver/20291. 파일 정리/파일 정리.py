N = int(input())
dic = dict()

for _ in range(N):
    line = input()
    for i in range(len(line)):
        if line[i] == '.':
            if dic.get(line[i+1:]):
                dic[line[i+1:]] += 1
            else:
                dic[line[i+1:]] = 1

rst = sorted(dic.items())
for key, val in rst:
    print(key, val)