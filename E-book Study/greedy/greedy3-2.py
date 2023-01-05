#입력 조건: 첫째 줄에 N(2<= N <= 1000) , M(1<=M <=10,000), K(1<= K <= 10,000) 자연수가 주어지며, 공백으로 구분
# 입력을 할 때,import sys  list(map(int, input().split())) 공백으로 구분하여 입력
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분. 단 각각의 자연수는 1이상 10,000이하의 수로 주어진다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.
# 출력 조건: 첫째 줄에 동빈이의 큰 수ㅡ이 법칙에 따라 더해진 답을 출력한다.

n, m ,k = map(int, input().split())
data =  list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m-=1
    if m == 0:
        break
    result += second
    m-= 1

print(result)
