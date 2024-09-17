N, K = map(int, input().split())

S = [0] + list(map(int, input().split()))
D = [0] + list(map(int, input().split()))

# P[D[i]] = S[i]

for _ in range(K):
    tmp = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        tmp[D[i]] = S[i]
    S = tmp

for i in range(1, N+1):
    print(S[i], end=" ")

