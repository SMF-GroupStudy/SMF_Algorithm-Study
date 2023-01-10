# 거스름돈 문제 사욜할 500원 100원 50원 10원 돈이 N일때, N은 항상 10의 배수이다. # 거슬러 줘야 할 동전의 최소 개수
import sys
# list(map(int, input().split())) 공백으로 구분하여 입력
n = 1260
#몫 변수
a = 0
coin = [500, 100, 50, 10]
# n // coin 하면 몫으로 개수가 나오니까 list for문을 활용해 1번 인덱스의 몫을 구하고, 나머지를 또 몫값을 계산
for i in coin:
    a += n // i
    n %= i
print(a)

