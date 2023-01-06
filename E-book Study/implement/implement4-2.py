
# 구현 4 - 2 시각

#시 분 초를 변수로 두고 조건문으로 제어 10으로 나눈 몫 -> 30~39 나머지3 - 3, 13, 23 ,33, 43, 53 하지만 33만 중복되기때문에 2번째 제어문에서 뺌
n = int(input())
count = 0
for s in range(n+1):
    for b in range(60):
        for c in range(60):
            if(s // 10 ==3 or b//10 == 3 or c //10 == 3):
                count+=1
                print(s,b,c, count)
            elif((s % 10 == 3 and s != 33) or (b != 33 and b %10) == 3 or (c != 33 and c % 10) == 3):
                count += 1
                print(s,b,c, count)

print(count)

'''
문자열로 03시 20분 35초 일때 032035로 3이 있는지 판별
이게 훨씬 좋은 알고리즘 같음. --> 문자열로 바꾸는 생각을 못함.
h = int(input())
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)
'''
