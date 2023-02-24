## 그래프 이론

* 그래프란? 노드와 노드 사이에 연결된 간선의 정보를 가지고 있는 자료구조
* 그래프의 구현 방법 
* 인접 행렬(Adjacency Matrix) : 2차원 배열을 사용하는 방식
* 인접 리스트(Adjacency List) : 리스트를 사용하는 방식
* 서로소 집합 : 공통 원소가 없는 집합
* Union 연산은 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 합집합 연산이다.
* Find 연산은 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산이다.
* 서로소 집합 연산: union-find 자료구조 (합치기 찾기)라고 불리기도 한다.
```bazaar
서로소 알고리즘
1. union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A,B를 확인한다.
    1.1 A와 B의 루트 노드 A, B를 각각 찾는다.
    1.2 A를 B의 부모 노드로 설정한다.(B가 A를 가르키도록 한다).
2. 모든 union(합집합) 연산을 처리할 때까지 1번 과정을 반복한다.
```

서로소 집합 알고리즘 소스코드
```bazaar
def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x
    # 두 원소가 속한 집합을 합치기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a<b:
            parent[b] = a
        else:
            parent[a] = b
    
    #노드의 개수와 간선(union 연산)의 개수 입력 받기
    v,e = map(int, input().split())
    parent = [0] * (v + 1) # 부모 테이블 초기화
    
    #부모테이블 상에서 부모를 자기자신으로 초기화
    for i in range(1, v+1):
        parent[i] = i
    # union 연산을 각각 수행
    for i in range(n):
        a,b = map(int, input().split())
        union_parent(parent, a, b)
    #각 원소가 속한 집합 출력
    print('각 원소가 속한 집합: ' end='')
    for i in range(1, v+1):
        print(find_parent(parent, i), end ='')
    
    print()
    
    #부모테이블 내용 출력
    print('부모 테이블:' , end ='')
    for i in range(1, v+1):
        print(parent[i], end='')
```

#### 크루스칼 알고리즘
크루스칼 알고리즘은 가장 적은 비용으로 모든 노드를 연결할 수 있는데, 그리디 알고리즘을 분류됨.
* 먼저 모든 간선에 대하여 정렬을 수행한 뒤에 가장 거리가 짧은 간선부터 집합에 포함시키면 된다.
* 이때 사이클을 발생시킬 수 있는 간선의 경우, 집합에 포함시키지 않는다.

1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.<br>
    2.1 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.<br>
    2.2 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.<br>
3. 모든 간선에 대하여 2번의 과정을 반복한다.
4. 시간 복잡도: O(ElogE)

#### 위상정렬
정렬 알고리즘의 일종으로 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘
* 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는것
* 시간 복잡도: O(V+E) 