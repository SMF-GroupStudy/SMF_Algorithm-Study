'''
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


t = int(input())
result_list = []

for _ in range(t):
    result = 0
    v, e = map(int, input().split())
    parent = [0] * (v + 1)
    for i in range(1, v + 1):
        parent[i] = i
    edges = []
    for _ in range(e):
        a, b = map(int, input().split())
        edges.append((a, b))
    for edge in edges:
        a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += 1
    result_list.append(result)

for result in result_list:
    print(result)
'''
########################################################
# 위 코드는 크루스칼 알고리즘을 사용한 것으로 시간 초과
# 아래 코드는 블로그에서 본 두 코드로 하나는 BFS
# 하나는 모든 국가가 연결되어 있기 때문에 사실 그냥 n-1 하면 답이었음 ;;
# 근데 시간초과 나옴 왜지??
########################################################

import sys
input = sys.stdin.readline

t = int(input())

from collections import deque


def bfs(start, plane):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        if visited.count(True) == n:
            return plane

        curr = q.popleft()

        for node in graph[curr]:
            if not visited[node]:
                q.append(node)
                plane += 1
                visited[node] = True


for _ in range(t):
    n, m = map(int, input().split())
    visited = [False] * (n + 1)

    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    p = bfs(1, 0)
    print(p)

'''
t = int(input())

for _ in range(t):
    v, e = map(int, input().split())
    
    for _ in range(e):
        a, b = map(int, input().split())

    print(v-1)
'''