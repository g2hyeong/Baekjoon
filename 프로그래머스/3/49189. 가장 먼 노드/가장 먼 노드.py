from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    isVisited = [0 for _ in range(n+1)]
    
    for y, x in edge:
        graph[x].append(y)
        graph[y].append(x)
        
    q = deque()
    q.append(1)
    isVisited[1] = 1
    
    while q:
        cur = q.popleft()
        for x in graph[cur]:
            if isVisited[x] == 0:
                q.append(x)
                isVisited[x] = isVisited[cur] + 1
    max = -1
    for i in range(1, n+1):
        if isVisited[i] > max:
            max = isVisited[i]
    answer = 0
    for i in range(1, n+1):
        if isVisited[i] == max:
            answer += 1
    
    return answer
    