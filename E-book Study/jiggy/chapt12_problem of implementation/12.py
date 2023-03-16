def solution(n, build_frame):
     pillar = [[0] * n for _ in range(n)]
     beam = [[0] * n for _ in range(n)]

     while build_frame:
          work = build_frame.pop(0)
          x, y, a, b = work
          if b == 1:
               if a == 0:
                    if y == 0:
                         pillar[x][y] = 1
                    else:
                         if pillar[x][y-1] == 1 or beam[x][y] == 1 or beam[x-1][y] == 1:
                              pillar[x][y] = 1
                         else:
                              continue
               elif a == 1:
                    if pillar[x][y-1] == 1 or pillar[x+1][y-1] == 1 or (beam[x-1][y] == 1 and beam[x+1][y] == 1):
                         beam[x][y] = 1
                    else:
                         continue
          else:
               if a == 0:
                    if pillar[x][y+1] == 1:
                         if beam[x][y+1] == 1 or beam[x-1][y+1] == 1:
                              pillar[x][y] = 0
                         else:
                              continue
                    elif (beam[x-1][y+1] == 1 and beam[x][y+1] == 0) or (beam[x-1][y+1] == 0 and beam[x][y+1] == 1):
                         continue
                    else:
                         pillar[x][y] = 0
               elif a == 1:
                    if 












plane = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1],
       [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
       [1, 1, 1, 0], [2, 2, 0, 1]]

print(solution(5, plane))
