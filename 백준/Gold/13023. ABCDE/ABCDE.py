import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs(graph, v, visited, cnt):
    global ans
    if cnt == 4: # 깊이가 4라면 ans를 1로 초기화
        ans = 1
        return 
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited,cnt+1)
            visited[i] = False # 다시 방문해보기 위해 False 로 (백트래킹?)

n,m = map(int,input().rstrip().split())
graph = [[] for i in range(n)]
ans = 0
# 그래프 초기화
for _ in range(m):
    a,b= map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 연결 간선이 4 이상일 때만 해당 문제의 조건이 성립할 수 있다.
if m >= 4:
    for node in range(n):
        visited = [False] * n
        visited[node] = True # 시작 노드 방문 처리
        dfs(graph, node, visited, 0) # DFS 시작
        if ans == 1: # 깊이가 4인게 있다면 멈춤
            break
print(ans)