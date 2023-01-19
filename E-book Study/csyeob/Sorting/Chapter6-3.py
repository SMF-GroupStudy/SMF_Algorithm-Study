n = int(input())
data = []
for i in range(n):
    data.append(input().split())

def setting(grade):
    return grade[1]

for i in range(len(data)):
    result = sorted(data, key = setting)

for i in range(len(data)):
    print(result[i][0], end=" ")

