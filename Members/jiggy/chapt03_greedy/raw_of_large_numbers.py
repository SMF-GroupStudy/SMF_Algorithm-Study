N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

a = len(data)
value_maximum = 0

quotient = M // K   # 몫
remain = M % K      # 나머지

if quotient % 2 == 0:
    value_maximum = (data[a-1] + data[a-2]) * K * (quotient / 2) + (data[a-1] * remain)
else:
    value_maximum = (data[a-1] * K * ((quotient / 2) + 1)) + (data[a-2] * K * (quotient / 2)) + (data[a-2] * remain)


value_maximum += data[a-quotient] * remain
print(value_maximum)

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
