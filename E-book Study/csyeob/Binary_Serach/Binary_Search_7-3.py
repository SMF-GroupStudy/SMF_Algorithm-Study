n, m = map(int, input().split())
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        result = 0
        #찾은 경우 중간점 인덱스 반환
        for i in array:
            if i-mid < 0:
                continue
            else:
                result += (i-mid)
        if result == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif target > result:
            end = mid - 1
        else:
            start = mid + 1
    return mid -1 ## 이부분을 생각해보면 길이의 -1을 해줘야 최대 m의 길이를 뽑을 수 있음

print(binary_search(array, m, 0, max(array)))


