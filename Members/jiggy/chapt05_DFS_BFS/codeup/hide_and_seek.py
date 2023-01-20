# 하나의 노드가 얼마나 깊이까지 가는지 모두 확인해서 최단시간을 찾으려면
# 모든 경로를 다 탐색해야하므로 비효율적이다. 즉 DFS 보다는 BFS 임을 생각한다.
# 동일 시간 내에서(동일 그래프 깊이) 가장 먼저 도착하는 경우가 생겼을 때가 최적 시간임을 알 수 있다.

from collections import deque

n, k = map(int, input().split())
MAX = 10 ** 5
dist = [0] * (MAX + 1)


def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            return dist[x]
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)


print(bfs())
