## 정렬 알고리즘

데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다. 
* 선택 정렬, 삽입 정렬 , 퀵 정렬, 계수 정렬 등이 있음.
* 면접에서도 단골 문제로 출제됨 
---
### 선택정렬
선택정렬은 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복함.<br>
```bazaar
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array): # i+1 부터 array의 길이까지
        if array[min_index] > array[j]:
            min_index = j
    array[i] , array[min_index] = array[min_index], array[i] # 스와프
```
<strong>여기서! 스와프란??</strong><br>
#0 인덱스와 1 인덱스의 원소 교체하기
```bazaar
array = [3,5] # 0, 1 인덱스 교환
array[0], array[1] = array[1], array [0]
```

시간 복잡도 : O(N^2) 2중 for문이 사용되었기 때문.<br>
시간복잡도에 따르면 <strong>파이썬 기본 정렬 라이브러리</strong>가 가장 빠름.
---
### 삽입정렬
데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입
```bazaar
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i,0,-1):#인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else:#자기보다 작은 데이터를 만나면 그 위치에서 멈춤.
            break
    print(array)
```
시간 복잡도: O(N^2) 이중 반복문 때문

---
### 퀵정렬
가장 많이 사용되는 알고리즘<br>
퀵정렬에서는 피벗이 사용된다. 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 <strong>'기준'</strong>이다.
<br>
왼쪽 리스트와 오른쪽 리스트를 피벗의 오른쪽은 큰수 왼쪽은 작은수로 분할 후, 피벗을 옮긴다.
그 이후 나눈 2개의 분할에서 또 퀵정렬을 시행
```bazaar
array = [7,5,9,0,3,1,6,2,4,8]
def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while left <= right:
    #피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
         #피벗 보다 작은 데이터를 찾을 땍까지 반복
         while right > start and array[right] >= array[pivot]:
            right -= 1
         if left > right: #엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
         else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
         #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        quick_sort(array, start, right, -1)
        quick_sort(array, right +1, end)
      
    quick_sort(array, 0, len(array) -1)
    print(array)
```
* 파이썬의 장점을 살린 퀵 정렬 소스
```bazaar
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) < = 1:
        return array
    
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] #피벗을 제외한 리스트
    
    left_side = [x for x in tail if x<= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```
시간복잡도: 평균 - O(NlogN) 최악 - O(N^2)

---
### 계수 정렬
특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘<br>
'데이터의 크기 범위가 제한 되어 정수 형태로 표현할 수 있을때'만 사용할 수 있다.
* 계수 정렬은 일반적으로 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다.
* <strong>데이터의 크기가 제한되어 있을 때</strong>에 한해서 데이터의 개수가 매우 많더라서 빠르게 동작함.

```bazaar
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

```
시간 복잡도: O(N + K) 공간 복잡도: O(N + K)

---
### 파이썬 정렬 라이브러리
sorted() 함수를 제공
* 퀵정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어졌음. O(NlogN)을 보장함.
```bazaar
array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)
```
