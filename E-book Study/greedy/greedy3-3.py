# 숫자 카드 게임

rows, cols = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(rows)]
select = []
for i in range(rows):
    select.append(min(arr[i]))
print (max(select))
