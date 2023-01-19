from collections import deque

m, n = map(int, input().split())

box = []
for _ in range(n):
    box.append(list(map(int, input().split())))

# 이동할 네 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0


def bfs():
    queue = deque()

    for x in range(n):
        for y in range(m):
            if box[x][y] == 1:
                queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append([nx, ny])


bfs()
for i in box:
    if 0 in i:
        print(-1)
        exit(0)
    count = max(count, max(i))
print(count - 1)
