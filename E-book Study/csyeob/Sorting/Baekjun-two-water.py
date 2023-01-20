from itertools import combinations
n = int(input())

water = list(map(int, input().split()))

water.sort()
result = []
two = list(combinations(water,2))

score = 0

for i in range(len(two)):
    result.append(abs(two[i][0] + two[i][1]))
    score = result.index(min(result))

print(two[score][0], two[score][1])

## 이것도 메모리초과... 알고있지만 일부러 걍 작성해봄.

