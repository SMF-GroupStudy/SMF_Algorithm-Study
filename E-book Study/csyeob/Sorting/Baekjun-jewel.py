# 각 보석의 무게 Mi
# 각 보석의 가격 Vi
# 가방 k개
# 가방에 담을 수 있는 최대 무게 Ci 가방에는 최대 한개의 보석만 넣기가능

n, k = map(int, input().split())
jewel = []
for i in range(n):
    jewel.append(list(map(int, input().split())))
c = []
for i in range(k):
    c.append(int(input()))


def setting(price):
    return price[1]


jewel = sorted(jewel, key=setting, reverse=True)
c.sort(reverse=True)

result = []

for i in range(n):
    for j in range(k):
        if jewel[i][0] <= c[j]:
            result.append(jewel[i][1])
            if len(result) == len(c):
                print(sum(result))
            break



