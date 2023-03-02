n = int(input())
coin = list(map(int, input().split()))
coin.sort()

result = 1

for i in coin:
    if result < i:
        break
    # 만들 수 없을때 break
    result = result + i

print(result)