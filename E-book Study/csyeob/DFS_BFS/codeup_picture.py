graph = []
for i in range(10):
    graph.append(list(map(str,input())))

y, x  = map(int, input().split())

def bfs(x, y):

            if x < 0 or y <0 or x >= 10 or y>= 10:
                return
            if graph[x][y] == '_':
                graph[x][y] = '*'
                bfs(x-1,y)
                bfs(x+1,y)
                bfs(x, y-1)
                bfs(x,y+1)


bfs(x,y)
for i in range(10):
    print(''.join(graph[i]))