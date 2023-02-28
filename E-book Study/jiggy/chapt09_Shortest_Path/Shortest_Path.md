최단 경로
=
**최단 경로(Shortest Path)** : 노드와 간선을 이용해 그래프에서 최단 경로를 찾아내는 알고리즘으로 코딩테스트에서는 다익스트라 최단 경로 알고리즘, 플로이드 워셜 알고리즘 유형만 알아도 어렵지 않게 해결할 수 있다.
> **다익스트라 알고리즘 :** 다익스트라 알고리즘은 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘이다.   
> 다익스트라 최단 경로 알고리즘은 '음의 간선'이 없을 때 정상적으로 동작한다.   
> 다익스트라 알고리즘은 기본적으로 그리디 알고리즘으로 분류된다. 매번 '가장 비용이 적은 노드'를 선택해서 임의의 과정을 반복하기 때문이다. 알고리즘의 원리를 간략히 설명하면 다음과 같다.
> 1. 출발 노드를 설정한다.
> 2. 최단 거리 테이블을 초기화한다.
> 3. 방문하지 않은 노드 중에서 최단 거리가 짧은 노드를 선택한다.
> 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
> 5. 위 과정에서 3과 4번을 반복한다.
## 다익스트라 알고리즘
### 방법 1. 간단한 다익스트라 알고리즘
- 시간 복잡도: O(V^2), V = 노드의 개수
- 첫 방법은 직관적인 방법으로 시작 노드에서 연결된 간선을 따라 모든 노드를 순차적으로 순회하는 선형 탐색 방식이다. 간선을 따라 노드를 탐색할 때 마다 최단 거리로 갱신해주는 방식이다. 
~~~python
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선의 정보를 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0   # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
~~~
### 방법 2 개선된 다익스트라 알고리즘
- 시간 복잡도 : O(ElogV), V = 노드의 개수, E = 간선의 개수
- 방법 2 개선된 다익스트라 알고리즘은 기존 간단한 방식과 작동 원리는 같다. 단지 현재 가장 가까운 노드 저장하기 위한 목적으로만 우선순위 큐를 추가로 사용해준다.
- 우선순위 큐 사용으로 이전 알고리즘과 다르게 get_smallest_node() 함수가 필요 없다.
~~~python
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선의 정보를 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:    # 큐가 비어있지 않다면
        # 가장 최단 거리인 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))



# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
~~~
## 플로이드 워셜 알고리즘
**Floyd-Warshall Algorithm :** 모든 지점에서 다른 모든 지점까지의 최단경로를 구해야하는 경우 사용하는 알고리즘이다.
- 시간 복잡도 : O(N^3)
- 다익스트라 알고리즘 -> 그리디, 플로이드 워셜 알고리즘 -> 다이나믹 프로그래밍
- 2차원 리스트를 통해 노드간 최단 경로를 갱신한다. 초기 리스트의 정보는 연결 유무와 간선의 거리만 알려주기 때문에 순차적으로 노드 x를 거쳐갈 경우 기존 값과 비교하여 최단 거리를 찾아간다.
~~~python
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그레프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=' ')
    print()
~~~
