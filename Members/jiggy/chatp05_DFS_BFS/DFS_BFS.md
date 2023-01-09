DFS/BFS
=
## 꼭 필요한 자료구조 기초
**탐색(search)** : 많은 양의 데이터 중에서 원하는 데이터를 찾는과정   
ex) 그래프, 트리 등의 자료구조 안에서 탐색하는 문제들   

**자료구조** - 데이터를 표현하고 관리하고 처리하기 위한 구조
ex) 스택, 큐 등
> 삽입(push) : 데이터를 삽입한다   
> 삭제(pop) : 데이터를 삭제한다

### 스택
**스택** : 선입후출, 후입선출의 구조를 갖는 자료구조   
~~~python
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)    # 최 하단 원소부터 출력
print(stack[::-1])   # 최 상단 원소부터 출력
~~~


### 큐
**큐** : 선입선출, 후입후출의 구조를 갖는 자료구조
~~~python
from collections import deque

# Queue 구현을 위해 dequeue 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
~~~

### 재귀 함수
**재귀 함수** : 자기 자신을 다시 호출하는 함수   
**점화식** : 특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현한 것
~~~python
def recursive_function(stop_val):
    stop_val += 1
    if stop_val == 30:
        return print('재귀 그만')
    else:
        print('재귀 함수를 호출합니다.')
        recursive_function(stop_val)

stop_val = 0
recursive_function(stop_val)
~~~

**재귀 함수를 활요한 DFS 예시**
~~~python
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    #1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1)
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    # n! = n * (n - 1)! 를 그대로 코드로 적성하기
    return n * factorial_recursive(n - 1)

# 각각의 방식으로 구현한 n! 출력(n=5)
print('반복적으로 구현: ', factorial_iterative(5))
print('재귀적으로 구현: ', factorial_recursive(5))
~~~

### DFS
**DFS** : 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘   
- **그래프** - **노드**와 **간선**으로 표현, 노드를 **정점**으로도 표현    
- **인접 행렬** - 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
- **인접 리스트** - 자려구조 연결 리스트를 통해 노드의 연결된 형태를 기록하는 방식
~~~python
# 인접 행렬
INF = 999999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# 인접 리스트
# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))

print(graph)
~~~
**인접 행렬은 접근성이 좋지만 불필요한 메모리가 자원을 차지한다.**   
- ex) 노드 1과 7이 연결되어 있는지 확인할 때 : graph[1][7]   

**인접 리스트는 접근성이 떨어지지만 메모리가 낭비되지 않는다.**   
- ex) 노드 1과 7이 연결되어 있는지 확인할 때 : 차례로 노드를 확인 해야 됨


> #### DFS 동작 과정 ( stack 을 활용함 )
> 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
> 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면서 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
> 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

### BFS
**BFS** : 너비 우선 탐색, 가까운 노드부터 탐색하는 알고리즘
> #### BFS 동작 과정 ( queue 을 활용함 )
> 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
> 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
> 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
    
|            |  **DFS**   |   **BFS**   |
|:----------:|:----------:|:-----------:|
| **동작 원리**  |     스택     |      큐      |
| **구현 방법**  |  재귀 함수 이용  |  큐 자료구조 이용  |




