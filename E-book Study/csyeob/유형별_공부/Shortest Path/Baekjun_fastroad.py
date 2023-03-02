import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

m, n = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, dis = map(int, input().split())
    if y <= n:
        ## 계속 오류가 났었는데 첫번째 예제에 151이 있어서 넘으면 제외 150까지임 길이가
        graph[x].append((y,dis))

for i in range(n):
    graph[i].append((i+1, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))



dijkstra(0)
print(distance[n])