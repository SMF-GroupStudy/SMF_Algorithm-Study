## 순차 탐색
리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법<br>
이미 순차탐색은 1장에서부터 사용해옴.<br>
* 순차탐색 코드

```bazaar
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target: 
        return i + 1 #현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)
        
    print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
    input_data = input().split()
    n = int(input_data[0]) #원소의 개수
    target = input_data[1] #찾고자 하는 문자열
    
    print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
    array = input().split()
    
    #순차 탐색 수행 결과 출력
    print(sequential_search(n,target, array))
```

## 이진탐색(Binary Search)
내부에 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘<br>
데이터가 무작위일 때는 사용할 수 없지만, 이미 정렬되어 있다면 매우 데이터를 빠르게 찾을 수 있다.
<br>
시작점, 끝점, 그리고 중간점, 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 게 이진 탐색 과정이다.
* 시간복잡도 : O(log N) <br>
한 단계를 거칠 때마다 절반씩 줄어든다는 점에서 퀵 정렬과 공통점이 있음.
<br>
<br>
* 재귀함수로 구현한 이진 탐색 
```bazaar
# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 적은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
#전체 원소 입력받기
array = list(map(int, intput().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result = None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```
* 반복문으로 구현한 이진탐색
```bazaar
# 이진 탐색 소스코드 구현(반복문)
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

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))
# 이진 탐색 수행 결과 출력
result = binary_search(array, target,0 , n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```
* 탐색 범위가 큰 상황에서 유용, 범위가 2000만을 넘어가면 이진 탐색으로 접근하는 것이 좋음
* 데이터의 개수나 값이 1000만 단위 이상으로 넘어가면 이진 탐색과 같이 O(logN)의 속도를 내야하는 알고리즘을 떠올려야함.

## 트리 자료구조
이진 탐색은 전제 조건이 데이터 정렬이다. 데이터베이스는 내부적으로 대용량 데이터 처리에 적합한 트리 자료구조를 이용하여 항상 데이터가 정렬되어 있다.
따라서 데이터베이스에서의 탐색은 이진 탐색과는 조금 다르지만, 이진 탐색과 유사한 방법으로 탐색을 항상 빠르게 수행하도록 설계되어 있어서 데이터가 많아도 탐색하는 속도가 빠르다.
<br>
책 192~193 참고<br>
 **왼쪽 자식노드<부모노드<오른쪽자식노드**가 성립해야지 이진 탐색 트리

### 빠르게 입력받기
이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 넓은 편이다서
1000만개를 넘어가거나 탐색 범위의 크기가 1000억 이상이면 이진 탐색 알고리즘을 의심해봐야함.
* 입력 데이터가 많은 개수라면 input()함수를 사용하면 동작 속도가 느려서 시간 초과로 오답 판정이 나옴.
* **sys 라이어브러리의 <code>**readline()함수**</code>를 사용해야함.**
```bazaar
import sys
# 하나의 문자열 데이터 입력 받기
input_data = sys.stdin.readline().rstrip()
# 입력받은 문자열 그대로 출력
print(input_data)
```
한 줄 입력 받고 나서 rstrip()함수를 꼭 호출해야한다. readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백문자를 제거하려면
rstrip()함수를 사용해야하다.