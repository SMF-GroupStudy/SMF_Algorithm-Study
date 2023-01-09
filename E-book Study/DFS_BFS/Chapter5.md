### Chapter5

#### 자료구조
* 스택: LIFO(후입 선출) 방식 stack<br>
```bazaar
stack = []
stack.append(5) # 5삽입
stack.pop() # 삭제
print(stack)
print(stack[::-1]) # 원소의 반대로 출력
```
* 큐: FIFO(선입 선출) 방식 Queue
```bazaar
from collections import deque

queue = deque()
queue.append(5) # 5삽입
queue.popleft() # 삭제
print(queue)
queue.reverse() # 역순 출력 
print(queue)
```
* 재귀 함수: DFS와 BFS를 구현하려면 재귀함수도 알아야 함. 자기 자신을 다시 호출하는 함수임
```bazaar
def recursive_function():
    print('재귀함술 호출')
    recursive_function()
recursive_function()
```
---
### DFS
깊이 우선 탐색 - 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
* 인접행렬: 2차원 배열로 그래프의 연결 관계를 표현하는 방식
* 인접 리스트: 리스트로 그래프의 연결 관계를 표현하는 방식
* 스택을 사용 O(N) 재귀 함수 이용
```bazaar
# 인접행렬 방식
INF = 99999999 # 무한 비용의 선언
# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5]
    [7, 0, INF(무한)]
    [5, INF, 0]
]
print(graph)
```
```bazaar
# 인접 리스트 방식
# 행이 3개인 2차원 리스트로 인접 리스트를 표현
graph = [[] for _ in range(3)]
#노드 0에 연결된 노드 정보 저장
graph[0].append((1,7))
graph[0].append((2,5))
```
### BFS
너비 우선 탐색 - 가까운 노드부터 탐색하는 알고리즘
* 큐를 사용 O(N) 큐 자료구조를 이용
* 실제 수행시간은 DFS보다 좋은 편이다.





















