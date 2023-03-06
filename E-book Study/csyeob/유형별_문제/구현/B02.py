#문자열 재정렬

# 문자열 s 입력
s = input()

result = sorted(s) # 정렬 하면 1 5 7 A B C K K 숫자부터 정렬됨.
alpha =""
num = 0
for i in range(len(result)):
    if str.isdigit(result[i]) == True: # 이 문자가 숫자이면 TRUE 반환
        num += int(result[i])
    else:
        alpha += result[i]

print(alpha, num, sep='')
