def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        #찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
n_data = list(map(int, input().split()))
# 틀린 부분 -> 이진 탐색을 수행하기 위해서는 정렬을 수행해야함....
n_data.sort()
m = int(input())
m_data = list(map(int, input().split()))



for i in range(m): # for i in m_data 이게 더 좋아 보임.
    result = binary_search(n_data, m_data[i], 0, n-1)
    if result == None:
        print('no', end=" ")
    else:
        print('yes', end=" ")
