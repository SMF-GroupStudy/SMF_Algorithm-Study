paint = []
for i in range(10):
    paint.append(list(map(str, input())))

x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, paint):
    if paint[x][y] == '*':
        return paint
    elif paint[x][y] == '_':
        paint[x][y] = '*'
        dfs(x - 1, y, paint)
        dfs(x, y - 1, paint)
        dfs(x + 1, y, paint)
        dfs(x, y + 1, paint)
        return paint
    return False


paint = dfs(x, y, paint)

for i in range(10):
    if i > 0:
        print()
    for j in range(10):
        print(paint[i][j], end='')
