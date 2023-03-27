from itertools import *

n, m = map(int, input().split())

weight = list(map(int, input().split()))
two = list(combinations(weight, 2))
result = 0
for i in range(len(two)):
    a, b = two[i]
    if a != b:
        result += 1

print(result)


