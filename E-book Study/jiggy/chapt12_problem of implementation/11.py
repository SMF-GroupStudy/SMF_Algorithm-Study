n = int(input())
k = int(input())

board = [[0] * n for _ in range(n)]
board[0][0] = 1

apple = []
for _ in range(k):
    a, b = map(int, input().split())
    apple.append((a, b))

l = int(input())

direction = []
for _ in range(l):
    x, c = map(str, input().split())
    direction.append((int(x), c))

time = 0
snake_d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
snake_i = 0
snake_x = 0
snake_y = 0
snake_tail = (snake_x, snake_y)
judge = 0
t, d = direction.pop(0)

while True:
    if judge == 1:
        if direction:
            t, d = direction.pop(0)
    if time == t:
        judge = 1
        if d == 'D':
            snake_i += 1
            if snake_i > 3:
                snake_i = 0
            snake_x += snake_d[snake_i][0]
            snake_y += snake_d[snake_i][1]

        if d == 'L':
            snake_i -= 1
            if snake_i < 0:
                snake_i = 3
            snake_x += snake_d[snake_i][0]
            snake_y += snake_d[snake_i][1]
    else:
        judge = 0
        snake_x += snake_d[snake_i][0]
        snake_y += snake_d[snake_i][1]

    if snake_x < 0 or snake_y < 0 or snake_x >= n or snake_y >= n:
        time += 1
        break

    board[snake_x][snake_y] += 1

    if board[snake_x][snake_y] == 2:
        time += 1
        break

    if (snake_x + 1, snake_y + 1) not in apple:
        board[snake_tail[0]][snake_tail[1]] = 0
        for tail in snake_d:
            tail_x = snake_tail[0] + tail[0]
            tail_y = snake_tail[1] + tail[1]
            if tail_x < 0 or tail_y < 0 or tail_x >= n or tail_y >= n:
                continue
            if board[tail_x][tail_y] == 1:
                snake_tail = (tail_x, tail_y)
            else:
                tail_x = snake_tail[0] - tail[0]
                tail_y = snake_tail[1] - tail[1]

    time += 1


print(time)
