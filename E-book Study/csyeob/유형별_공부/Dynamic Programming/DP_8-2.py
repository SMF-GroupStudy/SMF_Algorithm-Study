n = int(input())

food = list(map(int, input().split()))

d = [0] * 101

d[0] = food[0]
d[1] = max(food[0], food[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+food[i])

print(d[n-1])

## 코드는 책이랑 똑같음.. 왜냐 막혀서 봤더니
# d[1] = food[1] 로 했고, d[i] = max(d[i-2], d[i] + food[i]) 이렇게 했었는데 말이 안되긴함.