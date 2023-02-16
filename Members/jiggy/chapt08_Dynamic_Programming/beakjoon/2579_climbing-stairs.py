n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

d = [0] * 200 * 10000

d[0] = array[0]
d[1] = array[0] + array[1]

for i in range(2, n):
    d[i] = array[i] + max(d[i - 1], d[i - 2])

print(d[n - 1])
