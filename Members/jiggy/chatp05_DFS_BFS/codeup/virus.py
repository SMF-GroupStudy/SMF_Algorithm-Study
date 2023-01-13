computer = int(input())
connected_computer = int(input())

network = []
for i in range(connected_computer):
    network.append(list(map(int, input().split())))

infected = [False] * (computer+1)


def dfs(graph, v, visited):
    visited[v] = True

    for j in graph:
        if v in j:
            if not visited[j[0]]:
                visited[j[0]] = True
                dfs(graph, j[0], visited)
            elif not visited[j[1]]:
                visited[j[1]] = True
                dfs(graph, j[1], visited)

    return visited


print(sum(dfs(network, 1, infected))-1)
