n = int(input())
coin_list = list(map(int, input().split()))
coin_list.sort()

target = 1
for x in coin_list:
    if target < x:
        break
    target += x

print(target)
# 이게 어떻게 성립 하는거지
# 난 이건 모르겠다.. 이해 안되면 외우자;;
