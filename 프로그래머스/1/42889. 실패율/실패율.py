def solution(N, stages):
    failure = [0] * (N+1)
    cur = [0] * (N+1)
    tmp = []
    contender = len(stages)
    
    for stage in stages:
        for i in range(1, N+1):
            if stage == i:
                cur[i] += 1
                break
        
    for i in range(1, N+1):
        if contender != 0:
            failure[i] = cur[i] / contender
        else:
            failure[i] = 0
        contender = contender - cur[i]
        tmp.append((failure[i], i))
    
    tmp.sort()
    answer = []
    while len(tmp) > 0:
        cnt = 0
        for x, y in tmp:
            if x == tmp[-1][0]:
                answer.append(y)
                cnt += 1
        for _ in range(cnt):
            tmp.pop()
    
    return answer