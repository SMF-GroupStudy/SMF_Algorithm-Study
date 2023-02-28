def judge_same_team(parent, a, b):
    if parent[a] == parent[b]:
        return True
    else:
        return False


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_team(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = [0] * (n + 1)
for i in range(n+1):
    parent[i] = i

judge = []
for _ in range(m):
    command, student_a, student_b = map(int, input().split())

    if command == 0:
        union_team(parent, student_a, student_b)
    elif command == 1:
        judge.append(judge_same_team(parent, student_a, student_b))

for i in judge:
    if i:
        print('Yes')
    else:
        print('No')
