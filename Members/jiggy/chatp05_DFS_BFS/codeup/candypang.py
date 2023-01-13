from collections import deque

candy = []
for _ in range(7):
    candy.append(list(map(int, input().split())))

# 순서 대로 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, candy, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    color = candy[x][y]
    count = 1

    while queue:
        x, y = queue.popleft()

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if nx < 0 or ny < 0 or nx >= 7 or ny >= 7:
                continue

            if candy[nx][ny] == color and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1

    if count >= 3:
        return True
    else:
        return False


visited = [[False for _ in range(7)] for _ in range(7)]
res = 0

for i in range(7):
    for j in range(7):
        if not visited[i][j]:
            if bfs(i, j, candy, visited):
                res += 1

print(res)

