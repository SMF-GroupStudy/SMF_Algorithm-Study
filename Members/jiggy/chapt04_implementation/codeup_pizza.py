n = int(input())
a, b = map(int, input().split())
c = int(input())
d = []
for i in range(n):
    d.append(int(input()))


def price_pizza(A, B, K):
    return A + K * B


def kcal_pizza(C, D):
    return C + sum(D)


d.sort(reverse=True)
best_kcal = []
dow = []
for i in range(n):
    dow.append(d[i])
    one_dal_to_kcal = kcal_pizza(c, dow) / price_pizza(a, b, i+1)
    best_kcal.append(one_dal_to_kcal)

print(int(max(best_kcal)))
