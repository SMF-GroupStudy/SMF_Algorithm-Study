
n, k = map(int, input().split())
count = 0
while k <= n:
        if(n % k == 0):
            n = n // k
            count += 1
        else:
            n = n -1
            count += 1
while n > 1:
    n = n-1
    count += 1
print(count)
