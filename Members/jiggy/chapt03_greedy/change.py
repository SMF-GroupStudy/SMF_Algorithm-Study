import random

change = random.randint(0, 1000) * 10
print("거슬러 줘야 하는 금액: ", change)

change_list = [500, 100, 50, 10]
print("존재 하는 거스름 돈 단위: ", change_list)

min_count = 0

for i in change_list:
    count = change // i
    min_count += count
    change = change - i * count

print("거슬러 줘야 할 동전의 최소 개수: ", min_count)
