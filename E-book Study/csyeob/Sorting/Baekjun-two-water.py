# from itertools import combinations
# n = int(input())
#
# water = list(map(int, input().split()))
#
# result = []
# two = list(combinations(water,2))
#
#
# for i in range(len(two)):
#     result.append(abs(two[i][0] + two[i][1]))
#
# score = result.index(min(result))
#
# if two[score][0] < two[score][1]:
#     print(two[score][0], two[score][1])
# else:
#     print(two[score][1], two[score][0])
#
# ## sort를 하지 않았음에도 그냥 초과..
# ## 이것도 메모리초과... 알고있지만 일부러 걍 작성해봄.
#
n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

left = 0
right = n - 1

answer = abs(arr[left] + arr[right])
final = [arr[left], arr[right]]

while left < right:
    left_val = arr[left]
    right_val = arr[right]

    sum = left_val + right_val

    if abs(sum) < answer:
        answer = abs(sum)
        final = [left_val, right_val]
        if answer == 0:
            break
    if sum < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])