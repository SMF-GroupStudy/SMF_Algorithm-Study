n, m = map(int, input().split())

result_list = []
for i in range(n):
    card = list(map(int, input().split()))
    result_list.append(min(card))

print(max(result_list))
