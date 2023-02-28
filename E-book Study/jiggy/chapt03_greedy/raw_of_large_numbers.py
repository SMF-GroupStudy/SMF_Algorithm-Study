n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
a = len(data)

main_value = k * data[a-1] + data[a-2]
remain_value = (m % (k + 1)) * data[a-1]

large_number = (m // (k+1)) * main_value + remain_value

print(large_number)

'''
# 책에서 나온 풀이 내가 하려는 풀이와 비슷
# N, M, K를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N 개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k+1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)
'''

'''
# 책에 나온 첫 풀이
# N, M, K를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N 개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
'''
