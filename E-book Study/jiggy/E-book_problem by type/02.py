# 연산할 숫자 문자열로 입력 받기
s = input()

# 결과값 초기화
result = 0
# 문자열을 왼쪽부터 차례로 반복하여 연산
for i in s:
    # 0이나 1이거나 첫 연산일 경우 덧셈 연산
    if i == "0" or i == "1" or result == 0:
        result += int(i)
    # 아닐 경우 전부 곱셈 연산
    else:
        result *= int(i)

print(result)
