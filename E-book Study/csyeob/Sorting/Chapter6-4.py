n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def change(a, b, k):
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        a[i] = b[i]
    print(sum(a))

change(a,b,k)

