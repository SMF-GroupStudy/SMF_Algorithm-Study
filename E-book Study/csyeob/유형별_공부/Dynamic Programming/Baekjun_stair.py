n = int(input())

stairs = []
for i in range(n):
    stairs.append(int(input()))


d = [0] * 10001
if len(stairs) <= 2:
    print(sum(stairs))
else:
    d[0] = stairs[0]
    d[1] = stairs[0]+stairs[1]
#   d[2] = max(stairs[0]+stairs[2], stairs[0]+ stairs[1])
#   2번째까지 정해줌 처음엔

    for i in range(2, n):  ## 원랜 3이였음.
        d[i] = max(stairs[i] + stairs[i-1] + d[i-3], stairs[i] + d[i-2])

    print(d[n-1])

## 결국엔 if문 저거 없어서 틀린거긴함.