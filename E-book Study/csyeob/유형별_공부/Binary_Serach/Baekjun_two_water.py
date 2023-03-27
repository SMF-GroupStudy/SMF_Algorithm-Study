import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

start = 0
end = len(arr)-1

min = sys.maxsize

while start < end:
    # 여기서 <= 하면 안됨. 같은 특성의 용액을 2번더하는건 금지 되어있음.
    # mid를 굳이 안써도 풀 수 있음.... mid를 쓰면 오히려 어려워짐.
    # mid 써서 풀어서 해봤는데 틀림
    result = arr[start] + arr[end]
    if abs(result) < min:
        min = abs(result)
        answer = arr[start], arr[end]
    if result == 0:
        break
    if result < 0:
        start += 1
    else:
        end -= 1

for i in sorted(answer):
    print(i, end=' ')