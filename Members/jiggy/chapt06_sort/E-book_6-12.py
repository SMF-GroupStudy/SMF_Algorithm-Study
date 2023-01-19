n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] <= B[i]:
        A[i], B[i] = B[i], A[i]
    # else: break 이것도 넣어줘야 해 책에는 있던거

print(sum(A))
