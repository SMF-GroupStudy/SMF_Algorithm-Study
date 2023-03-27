s = input()
num_list = []

for i in range(len(s)):
    num = int(s[i])
    num_list.append(num)

result = 0
if len(num_list) > 1:
    if num_list[0] + num_list[1] > num_list[0] * num_list[1]:
        result = num_list[0] + num_list[1]
    else:
        result = num_list[0] * num_list[1]
else:
    result = num_list[0]

if len(num_list) > 2:
    for i in range(2, len(num_list)):
        if result + num_list[i] > result * num_list[i]:
            result = result + num_list[i]
        else:
            result = result * num_list[i]

print(result)