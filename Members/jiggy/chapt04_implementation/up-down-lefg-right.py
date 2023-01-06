# 입력 조건
# 첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1<=N<=100)
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1<=이동횟수<=100)

# 출력 조건
# 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X, Y)를 공백으로 구분하여 출력한다.

# 나의 문제 접근 방식
# 이동 계획을 리스트로 받아 for 문으로 순차적으로 돌린다.
# 이동에 따라 여행자의 좌표값을 변경해 준다. 

N = int(input())
command_list = list(map(str, input().split()))

x, y = 1, 1

for i in command_list:
    if i == 'U':
        if x <= 1:
            print("지도를 벗어나는 명령입니다.")
        else:
            x -= 1

    if i == 'D':
        if x >= N:
            print("지도를 벗어나는 명령입니다.")
        else:
            x += 1

    if i == 'R':
        if y >= N:
            print("지도를 벗어나는 명령입니다.")
        else:
            y += 1

    if i == 'L':
        if y <= 1:
            print("지도를 벗어나는 명령입니다.")
        else:
            y -= 1

print(x, end=' ')
print(y, end=' ')
