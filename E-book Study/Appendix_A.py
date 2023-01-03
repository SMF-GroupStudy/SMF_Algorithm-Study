# 수 자료형의 연산
a = 7
b = 3
# 나누기
print(a/b)
#나머지
print(a&b)
#몫
print(a//b)
#거듭제곱 연산자 **
print(a ** b)

#리스트 선언
c = [1,2,3,4,5,6,7,8,9]
print(c)
# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
d = [0] * n
print(d)
# 리스트 컴프리헨션
# 리스트를 초기화하는 방법 중 하나
array = [ i for i in range(20) if i % 2 == 1]
print(array)

array1 = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array1)
## 위의 코드보다 훨씬 간결하고 짧음.

# 리스트 관련 메서드
# append() - 변수명.append() - 리스트에 원소를 하나 삽입할 때 사용한다. O(1)
# sort() - 변수명. sort() - 기본 정렬 기능으로 오름차순으로 정렬한다. O(NlogN)
# sort() - 변수명.sort(reverse = True) - 내림차순으로 정렬 O(NlogN)
# reverse() - 변수명.reverse() - 리스트의 원소의 순서를 모두 뒤집어 놓는다. O(N)
# insert() - 변수명.insert(삽입할 위치 인덱스, 삽입할 값)- 특정한 인덱스 위치에 원소를 삽입할 때 사용 - O(N)
# count() - 변수명.count(특정 값) - 리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 사용 - O(N)
# remove() - 변수명.remove(특정 값) - 특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러 개면 하나만 제거한다 - O(N)

e = [1, 4, 3]
print("기본 리스트 :", e)
#리스트 원소 삽입 append
e.append(2)
print("삽입:", e)
#오름 차순 정렬 sort
e.sort()
print("오름차순 정렬: ", e)
#내림 차순 정렬 sort(reverse = True)
e. sort(reverse=True)
print("내림차순 정렬:",e)
#리스트 원소 뒤집기 reverse()
e.reverse()
print("원소 뒤집기: ",e)
#특정 인덱스에 데이터 추가 insert(a, b)
e. insert(2, 3)
print("인덱스 2에 3 추가: ",e)
# 특정 값인 데이터 개수 세기 , count()
print("값이 3인 데이터의 개수:", e.count(3))
# 특정 값 데이터 삭제
e. remove(1)
print("값이 1인 데이터 삭제: ", e)
