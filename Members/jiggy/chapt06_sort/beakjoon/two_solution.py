n = int(input())
solutions = list(map(int, input().split()))
INF = 1000
array = []
for i in range(n):
    for j in range(n):
        if i == j:
            array.append(INF)
        else:
            array.append(abs(solutions[i] + solutions[j]))

res = [solutions[(array.index(min(array))) // n], solutions[(array.index(min(array))) % n]]
res.sort()
print(res[0], end=' ')
print(res[1])
