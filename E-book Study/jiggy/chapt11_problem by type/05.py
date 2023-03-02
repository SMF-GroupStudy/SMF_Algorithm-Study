n, m = map(int, input().split())

bowling = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(n):
        if bowling[i] == bowling[j] or j <= i:
            continue
        else:
            count += 1

print(count)
