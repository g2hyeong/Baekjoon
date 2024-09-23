def DFS(start, graph, isVisited):
    isVisited[start] = 1
    for next in range(len(graph[start])):
        if graph[start][next] == 1 and isVisited[next] == 0:
            DFS(next, graph, isVisited)
            
def solution(n, computers):
    isVisited = [0] * n
    cnt = 0
    for i in range(n):
        print(isVisited)
        if isVisited[i] == 0:
            DFS(i, computers, isVisited)
            cnt += 1
    return cnt