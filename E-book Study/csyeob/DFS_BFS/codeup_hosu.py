from collections import deque

w, h = map(int, input().split())

lake = []
for i in range(h):
    lake.append(list(map(str, input().split())))

visit = [[0 for _ in range(w)] for _ in range(h)]
dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
# 대각선까지 생각해야하므로 저렇게 방향을 설정함.

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    visit[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            if lake[nx][ny] == 'L' and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append([nx,ny])


result = 0
for i in range(h):
    for j in range(w):
        if visit[i][j] == 0 and lake[i][j] == 'L':
            bfs(i,j)
            result += 1

print(result)