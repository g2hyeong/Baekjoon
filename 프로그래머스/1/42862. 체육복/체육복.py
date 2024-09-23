def solution(n, lost, reserve):
    student = [1] * n
    for x in lost:
        student[x-1] -= 1
    for x in reserve:
        student[x-1] += 1
    
    for i in range(n):
        if student[i] > 1:
            d = [-1, 1]
            for j in range(2):
                if 0 <= i+d[j] < n:
                    if student[i+d[j]] == 0 and student[i] > 1:
                        student[i+d[j]] += 1
                        student[i] -= 1
    print(student)
    answer = n - student.count(0)
    return answer