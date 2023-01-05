# 숫자 카드 게임
import time
rows, cols = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(rows)]
select = []
start_time = time.time()
for i in range(rows):
    select.append(min(arr[i]))
print (max(select))
end_time = time.time()
print("time: ", end_time-start_time)