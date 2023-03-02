from collections import deque

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
def bfs():
    queue = deque()
    # 처음 토마토 익은거 넣기 이 부분 생각 못해서 안풀림
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append([i, j])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 안익은거를 익은걸로 바꾸기
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])


bfs()
for i in graph:
    if 0 in i:
        print(-1)
        exit(0)
    count = max(count, max(i))

print(count - 1)

