import time
n, k = map(int, input().split())
count = 0
start_time = time.time()
num = n - 1
count += 1
while k <= num:
        num = num // k
        count += 1

print(count)
end_time = time.time()
print("time: ", end_time-start_time)