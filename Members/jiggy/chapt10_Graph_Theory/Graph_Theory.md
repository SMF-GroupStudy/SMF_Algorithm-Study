그래프 이론
=
해당 챕터에서는 앞에서 배운 내용을 토대로 다양한 그래프 알고리즘을 배울 것이다.   
내용으로는 크루스칼 알고리즘, 위상 정렬 알고리즘 등이 있다.   
그 외 알고리즘 문제를 풀 때 개체간 연결된 내용의 문제는 그래프 문제라 생각하고, 노드와 간선을 선정하여 그래프를 만들어 풀어야 한다.
### 그래프(Graph)
> 그래프(Graph) : 노드(Node)와 노드 사이에 연결된 간선(edge)의 정보를 가지고 있는 자료구조를 의미한다.

자료구조 중 트리(Tree)자료구조는 다양한 알고리즘에 사용되므로 꼭 기억해야 한다.
>최소 힙: 항상 부모 노드가 자식 노드의 크기보다 작은 자료구조  
>최대 힙: 항상 부모 노드가 자식 노드의 크기보다 큰 자료구조

트리 자료구조는 부모에서 자식으로 내려오는 계층적인 모델에 속한다.
    
|                 |      **그래프**      |  **트리**   |
|:---------------:|:-----------------:|:---------:|
|     **방향성**     | 방향 그래프 혹은 무방향 그래프 |  방향 그래프   |
|     **순환성**     |     순환 빛 비순환      |    비순환    |
| **루트 노드 존재 여부** |     루트 노드가 없음     | 루트 노드가 존재 |
|   **노드간 관계성**   |   부모와 자식 관계 없음    | 부모와 자식 관계 |
|   **모델의 종류**    |      네트워크 모델      |   계층 모델   |

그래프의 구가지 구현 방식 및 시간 복잡도(노드의 개수가 V 간선의 개수가 E일 때)
> 인접 행렬(Adjacency Matrix)
> - 2차원 배열을 사용하는 방식
> - 시간 복잡도: O(V^2)
> - 특정 노드에서 노드로 이동할 때 드는 간선의 비용을 아는데 O(1)
> 
> 인접 리스트(Adjacency List)
> - 리스트를 사용하는 방식
> - 시간 복잡도: O(E)
> - 특정 노드에서 노드로 이동할 때 드는 간선의 비용을 아는데 O(V)

### 서로소 집합 (Disjoint Sets)
> 서로소 집합(Disjoint Sets) : 이란 공통 원소가 없는 두 집합을 의미하고, 서로소 집합 자료구조는 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조라고 할 수 있다.   

서로소 집합 자료구조는 union과 find 이 2개의 연산으로 조작할 수 있다.   
스택(stack)과 큐(queue)가 각각 push(넣기)와 pop(꺼내기) 연산으로 이루어졌던 것처럼, 서로소 집합 자료구 합집합과 찾기 연산으로 구성된다.   
그래서 서로소 집합 자료구조는 union-find(합치기 찾기) 자료구로라고 불리기도 한다. 
- union(합집합): 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산.
- find(찾기): 특정한 원소가 속한 집이 어떤 집합인지 알려주는 연산.  

서로소 집합 자료구조를 구현할 때는 트리 자료구조를 이용하여 집합을 표현하는데, 서로소 집합 정보(합집합 연산)가 주어졌을 때 트리 자료구조를 이용해서 집합을 표현하는 서로소 집합 계산 알고리즘과 코드는 다음과 같다. 
> 1. union(합집합) 연산을 하여, 서로 연결된 두 노드 A, B를 확인한다.   
> 	I A와 B의 루트노드 A', B'를 각각 찾는다.   
> II A'를 B'의 부모 노로 설정한다.(B'가 A'를 가르키도록 한다.)
> 2. 모든 union(합집합) 연산을 처리할 때 까지 1번 과정을 반복한다.


~~~python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
~~~
해당 코드에서 가장 밑에 있는 자식노드에서 최상위 부모노드를 찾는데 걸리는 시간 복잡도는 O(VM)이 된다(노드의 수 V * find or union 개수 M). 이를 해결하기 위해 경로 압축 기법을 사용한다.
~~~python
# find 함수에서 if문 내부에서 루트노드를 찾을 때까지 재귀 호출 한다.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
~~~
### 서로소 집합을 활용한 사이클 판별
union 연산은 그래프에서 간선으로 표현될 수 있다. 따라서 간선을 하나씩 확인하면서 두 노드가 포함되어 있는 집합을 합치는 과정을 반복하는 것만으로도 사이클을 판별할 수 있다. 알고리즘은 다음과 같다.
1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.   
I 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.   
II  루트 노드가 서로 같다면 사이클(Cycle)이 발생한 것이다. 
2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다.

이러한 사이클 판별 알고리즘은 방향성이 없는 무뱡향 그래프에만 적용 가능하며 간선의 개수가 E일 때, 매 간선마다 union 및 find 함수를 호출하는 방시긍로 동작한다.
~~~python
# judge_cycle
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b

        
v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')
~~~

### 신장 트리(Spanning Tree)
> 신장 트리(Spanning Tree): 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

### 크루스칼 알고리즘(Kruskal Algorithm)
신장 트리 중에서 최소 비용으로 만들 수 있는 신장트리를 찾는 알고리즘을 '최소 신장 트리 알고리즘' 이라고 하는데, 이 중 대표적은 알고리즘으로 Kruskal Alhorithm이 존재한다.
> 크루스칼 알고리즘(Kruskal Algorithm): 그리디 알고리즘으로 분류되고, 모든 간선에 대해 정렬을 수행한 뒤 거리가 가장 짧은 간선부터 집합에 포함시킨다. 이때 사이클을 발생할 수 있는 간선은 집합에 포합시키지 않는다.
> ### 구체적 알고리즘
> 1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
> 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
> I. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다. 
> II. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
> 3. 모든 간선에 대하여 2번 과정을 반복한다.   

- 최소 신장 트리의 비용을 구하는 크루스칼 알고리즘 코드. 👇🏻
~~~python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
~~~
크루스칼 알고리즘의 시간복잡도는 E개의 간선을 정렬할 때 가장 오랜 시간을 차지하고 다음과 같다.   
#### <center>O(ElogE)</center>


### 위상 정렬(Topology Sort)
> 위상 정렬(Topology Sort): 정렬 알고리즘의 일종. 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용하는 알고리즘.   
> 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
> - 진입 차수(Indegree): 특정 한 노드로 '들어오는' 간선의 개수
> ### 위상 정렬 알고리즘
> 1. 진입 차수가 0인 노드를 큐에 넣는다.
> 2. 큐가 빌 때까지 다음 과정을 반복한다.   
> I. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.   
> II. 새롭게 진입 차수가 0이 된 노드를 큐에 넣는다.   
> 
> 여기서 모든 원소를 방문하기(큐에서 원소가 V번 추출되기) 전 큐가 빈다면 사이클이 존재한다고 판단할 수 있다.

위상 정렬은 큐에서 추출된 원소의 순서를 의미하고, 큐에 삽입하는 순서에 따라 복수의 답이 존재할 수 있다.
~~~python
from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()
~~~

위상 정렬의 시간복잡도는 모든 노드를 확인하면서, 해당 노드의 출발하는 간선을 차례대로 제거해야 하고, 다음과 같다.
#### <center>O(V + E)</center>

