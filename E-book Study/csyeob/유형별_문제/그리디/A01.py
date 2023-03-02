n = int(input())
user = list(map(int, input().split()))
user.sort()

group = 0
result = 0
for i in user:
    group += 1
    if group >= i:
        result += 1
        group = 0

print(result)