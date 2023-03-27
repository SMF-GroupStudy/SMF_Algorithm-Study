#컴퓨터의 수
n = int(input())
#간선의 수
m = int(input())
#부모테이블 초기화
parent = [0] * (n+1)
#특정 원소 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
#두 원소 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
#간선을 담는 변수
edges = []
result = 0
# 부모테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i
#간선 정보
for i in range(m):
    a, b, cost = map(int, input().split())
    #비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

#간선을 비용순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost


print(result)
