# 보드의 크기
n = int(input())
k = int(input())
rotate = [] # 방향 정보
# 보드
board = [[0] * (n+1) for _ in range(n + 1)]
# 사과의 위치
for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1
# 방향 변환 횟수 L
l = int(input())
for _ in range(l):
    x, c = input().split()
    rotate.append((int(x), c))

# 방향
dx = [0, 1, 0, -1] # 오른쪽 부터이기 때문에 밑 오른쪽 위 오른쪽
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction -1) % 4
    else:
        direction = (direction +1) % 4
    return direction

def simulate():
    # 뱀의 첫 위치 맨위 맨 왼쪽
    x, y = 1, 1
    board[x][y] = 2  # 처음 위치
    time = 0  # 시간
    direction = 0  # 동쪽을 보고 있음.
    index = 0 #회전 정보
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx and nx <=n and 1 <= ny and ny <= n and board[nx][ny] != 2:
            # 사과가 없으면 이동 후 꼬리 제거
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
            # 사과가 있다면 이동 후 꼬리 그대로 두기
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx,ny))

            # 벽이나 뱀의 몸통과 부딪히면
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치 이동
        time += 1
        # 회전할 시간인 경우 회전
        if index < 1 and time == rotate[index][0]:
            direction = turn(direction, rotate[index][1])
            index += 1

    return time

print(simulate())







