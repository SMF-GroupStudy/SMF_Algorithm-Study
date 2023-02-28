n = int(input())
array = []
for i in range(n):
    N = int(input())
    if 0 <= N <= 500:
        array.append(N)
    else:
        i -= 1

array.sort(reverse=True)
for i in array:
    print(i, end=' ')
