# 문제: 00시 00분 00초 부터 입력받은 정수 N에 대하여 N시 59분 59초 까지 에서 3이 포함된 모든 경우의 수를 구하라.
# 입력 조건: 첫째 줄에 정수 N (0<=N<=23)
# 출력 조건: 3이 포함된 경우의 수 출력

# 나의 문제 풀이:
# 3이 포함된 시간과 안된 시간의 경우의 수를 직접 구해 N에 따라 경우의 수 출력
# 3이 포함된 시간과 안된 시간의 경우의 수를 연습장에 직접 계산하여 구한 단점이 있음.

N = int(input())

cases = 600 + 300 + 450 + 225
include_three_h = 6 * 10 * 6 * 10

if N == 0:
    cases = cases
elif 0 < N < 3:
    cases *= N
elif 3 <= N < 13:
    cases = N * cases + include_three_h
elif 13 <= N < 23:
    cases = (N - 1) * cases + include_three_h * 2
elif N == 23:
    cases = (N - 2) * cases + include_three_h * 3

print(cases)

'''
# 교제에서 제시한 문제 풀이
# 이게 더 깔끔한 것 같다.
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
'''
