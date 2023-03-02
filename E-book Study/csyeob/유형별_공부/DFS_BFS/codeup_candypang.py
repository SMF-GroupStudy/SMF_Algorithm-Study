from collections import deque
graph = []
for i in range(7):
    graph.append(list(map(int, input().split())))

visit = [[0 for _ in range(7)] for _ in range(7)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, value):
    queue = deque()
    queue.append([x,y])
    visit[x][y] = 1

    count = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 7 or ny >= 7:
                continue
        # 같은 색상 이면서 아직 방문 안함
            if visit[nx][ny] == 0 and graph[nx][ny] == value:
                visit[nx][ny] = 1
                queue.append([nx, ny])
                count += 1

    return count

result = 0
for i in range(7):
    for j in range(7):
        if visit[i][j] == 0:
            if bfs(i, j, graph[i][j]) >= 3:
                result += 1

print(result)