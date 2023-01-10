from collections import deque

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
result = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    global result
    queue = deque([start])
    visited[start] = True
    while queue:
        v= queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                result+=1
    print(result)

visited = [False]*(n+1)
bfs(graph,1,visited)