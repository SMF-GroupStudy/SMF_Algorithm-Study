# 문제는 a1을 입력 받았을 때 체스 나이트가 8*8 체스판에서 이동할 수 있는 경우의 수를 구하는 것.
# 책에서는 나이트가 이동할 수 있는 경우의 수를 리스트로 잘 정리하여 간단히 풀이
# 나는 나이트의 위치에 따라 모든 경우를 나누어 복잡한 풀이 선택
# 또, 알파벳을 int로 쉽게 변환해주는 코드를 몰라서 복잡해짐

night = list(input())

x, y = night[0], night[1]
y = int(y)

# 알파벳 int형으로 쉽게 변환하는 방법
# pos = input()
# row = int(pos[1])
# column = int(ord(pos[0])) - int(ord('a')) + 1

x_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in x_list:
    if x == i:
        index = x_list.index(i)
        x = index + 1
x = int(x)

count = 0
if 2 < x < 7:
    if 2 < y < 7:
        count = 8
    elif y == 2 or y == 7:
        count = 6
    elif y == 1 or y == 8:
        count = 4
elif x == 2 or x == 7:
    if 2 < y < 7:
        count = 6
    elif y == 2 or y == 7:
        count = 4
    elif y == 1 or y == 8:
        count = 3
elif x == 1 or x == 8:
    if 2 < y < 7:
        count = 4
    elif y == 2 or y == 7:
        count = 3
    elif y == 1 or y == 8:
        count = 2

print(count)

'''
# 책에서 제시한 코드

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [
    (-2, -1), (-1, -2), (1, -2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)
'''
