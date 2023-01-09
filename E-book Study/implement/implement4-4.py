# 구현 4- 4 게임개발
## 바로 밑 망작

n, m  = map(int, input().split())
x, y, direction = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 0, 1, 0] # 북 동 남 서 -> 북일땐 -1 남일땐 +1
dy = [0, 1, 0, -1] # 북 동 남 서 -> 동일땐 +1 서일땐 -1
'''
result = 0

while True:
    map[x][y] = 2
    # 뒤쪽에 바다이면서 왔던 곳이면 return
    for i in range(4):
        pos_x = x + dx[direction]
        pos_y = y + dx[direction]
        if pos_x > 0 and pos_x < n and pos_y > 0 and pos_y < n:
            if map[pos_x][pos_y] == 0:
                result += 1
                map[pos_x][pos_y] = 2
            else:
                direction += 1
                if direction > 3:
                    direction = direction - 3
    if map[pos_x][pos_y] == 2:
        direction -= 1
        if direction > 3:
            direction = direction - 3
        if map[pos_x][pos_y] == 1:
            break
print(result)
'''
## 일단 알고리즘을 짜봤는데 너무 어려워서 답지를 참고해서 밑에로 다시 짜봄.
## 방문 리스트
d = [[0] * m for _ in range(n)]
d[x][y] = 1
# 왼쪽 회전을 함수로 만드는게 더 나은거 같긴 했지만 위에 코드가 break를 써도 빠져나오질 못함 그래서 함수가 나은듯
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

result = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 후 안 가보고, 육지일때
    if d[nx][ny] == 0 and map[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        result += 1
        turn_time = 0
        continue
    # 회전 후다 가 보고 바다인 경우
    else:
        turn_time += 1
    # 4방향 다 못가는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있으면 이동
        if map[nx][ny] == 0:
            x = nx
            y = ny
        #바다로 막혔을때
        else:
            break
        turn_time = 0

print(result)






