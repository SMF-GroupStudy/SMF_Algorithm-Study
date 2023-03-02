num = input()

count_0 = 0
count_1 = 0

for i in range(0, len(num)-1):
    if num[i] != num[i+1]:
        if num[i+1] == '0':
            count_1 += 1
        else:
            count_0 += 1

print(min(count_1, count_0))
