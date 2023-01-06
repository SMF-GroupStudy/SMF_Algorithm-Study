#구현 4-3 왕실의 나이트
n = input()
count = 0
pos_cols = int(ord(n[0])) -96
pos_rows = int(n[1])
print(pos_cols, pos_rows)
move = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
for pos in move:
    if(pos[0] + pos_cols > 0 and pos[0] + pos_cols< 8 ):
        if(pos[1] + pos_rows > 0 and pos[1] + pos_rows < 8):
            count+=1
print(count)

## a를 숫자로 변환할 수 있으면 좋을거같아서 구글링 그 뒤로 저 좌표를 리스트에 담을 수 있는지 몰라서
# 막하다가 막혀서 뒤에 답지 참고


