n, k = map(int, input().split())
count = 0


def minus_one(N):
    return N - 1


def divide_n(N, K):
    return N / K


while n != 1:
    print(n)
    print(k)
    if n % k == 0:
        divide_n(n, k)
        count += 1
    else:
        minus_one(n)
        count += 1

print(count)
