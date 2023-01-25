
n = int(input())
parts = list(map(int, input().split()))
m = int(input())
estimate = list(map(int, input().split()))

# 내 코드
for i in range(m):
    for j in range(n):
        if estimate[i] == parts[j]:
            print('yes', end=' ')
            break
        elif j == (n-1):
            print('no', end=' ')

'''
# 책 코드
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in estimate:
    result = binary_search(parts, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
'''
