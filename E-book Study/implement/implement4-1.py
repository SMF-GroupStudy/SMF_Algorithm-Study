
#구현 4 -1 여행가의 계획
# 내가 푼 방법 - 굳이 좌표를 리스트에 넣어서 생각 하지 않고 x y좌표를 변수로 지정해서 조건문으로 제약 조건을 주어줌
# L 일때 y좌표 -1( y > 1 일때만) R일때 y좌표 +1 (y < n일때만) U 일때 x좌표 -1(x >1일때만) D 일때 x좌표 +1( x < n 일때)

n = int(input())
data =  list(input().split())
current_x, current_y = 1, 1
for i in data:
    if(i == 'L' and current_y > 1): current_y -= 1
    if(i == 'R' and current_y < n): current_y += 1
    if(i == 'U' and current_x > 1): current_x -= 1
    if(i == 'D' and current_x < n): current_x += 1

print(current_x, current_y)

# 책풀이
'''
n = int(input())
x,y = 1,1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny <1 or nx > n or ny > n:
        continue
    #이동 수행
    x, y = nx, ny

print(x, y)
'''



