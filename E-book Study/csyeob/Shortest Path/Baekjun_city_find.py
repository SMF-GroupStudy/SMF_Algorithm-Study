## 소개팅 자리를 거쳐가는 것이기 때문에 플로이드워셜을 써야함.

import sys
input = sys.stdin.readline

INF = int(1e9)

n, m, k, x = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for t in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][t] + graph[t][b])

result = []
for i in range(1, n+1):
    if graph[x][i] == k:
        result.append(i)
        print(i)

if len(result) == 0:
    print(-1)