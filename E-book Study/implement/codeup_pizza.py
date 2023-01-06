n = int(input())
a, b  = map(int, input().split())
# a 도우의 가격 b 토핑의 가격
c = int(input())
# 도우 열량
di = [list(map(int, input().split())) for _ in range(n)]
# 토핑 열량들
di.sort(reverse=True)
total_calory = c
total_price = a
c_p = total_calory/total_price

for i in di:
    if (c_p < (i[0] / b)):
        total_price += b
        total_calory += i[0]
        c_p = total_calory / total_price

print(int(c_p))

