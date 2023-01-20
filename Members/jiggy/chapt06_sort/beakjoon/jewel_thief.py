n, k = map(int, input().split())
jewels = []
for _ in range(n):
    jewel = input().split()
    jewels.append((int(jewel[0]), int(jewel[1])))
bags = []
for _ in range(k):
    bags.append(int(input()))

jewels.sort(reverse=True, key=lambda x: x[1])
bags.sort()

res = 0
for weight in jewels:
    for i in range(k):
        if (bags[i] - weight[0]) >= 0:
            res += weight[1]
            break
        else:
            continue

print(res)
