import copy
from collections import deque

n = int(input())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
# 각 강의의 고유 시간 저장
time = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:    # 인덱스 1부터  값 -1  전까지
        # 선수 강의가 있는 강의만 진입 차수 +
        indegree[i] += 1
        # 그래프
        graph[x].append(i)


def topology_sort():
    # 리스트를 복사할 때는 단순 대입 연산할 때 문제가 발생하는 경우가 있는데, 이를 방지해주는 deepcopy() 함수를 사용
    result = copy.deepcopy(time)
    q = deque()

    for j in range(1, n + 1):
        if indegree[j] == 0:
            q.append(j)

    while q:
        now = q.popleft()
        for k in graph[now]:
            # 선수 강의의 강의시간을 포함해주는 연산인거 같음
            result[k] = max(result[k], result[now] + time[k])
            indegree[k] -= 1
            if indegree[k] == 0:
                q.append(k)

    for u in range(1, n + 1):
        print(result[u])


topology_sort()
