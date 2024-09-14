switch_cnt = int(input())
switch = [0] + list(map(int, input().split()))
student_cnt = int(input())
student = list(tuple(map(int, input().split())) for _ in range(student_cnt))

def MAN(num):
    for i in range(1, switch_cnt+1):
        if i % num == 0:
            switch[i] = int(abs(switch[i] - 1))

def WOMAN(num):
    cnt = 0
    switch[num] = int(abs(switch[num] - 1))
    while True:
        cnt += 1
        if num - cnt <= 0 or num + cnt > switch_cnt:
            break
        if switch[num-cnt] == switch[num+cnt]:
            switch[num - cnt] = int(abs(switch[num - cnt] - 1))
            switch[num + cnt] = int(abs(switch[num + cnt] - 1))
        else:
            break

for sex, num in student:
    if sex == 1:
        MAN(num)
    else:
        WOMAN(num)

for i in range(1, switch_cnt+1):
    print(switch[i], end=" ")
    if i%20 == 0:
        print()