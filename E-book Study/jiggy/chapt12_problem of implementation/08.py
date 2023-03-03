# sub()함수를 사용하기 위해 정규표현 모듈 re import
import re

# 문자열 입력
n = input()

# 문자열을 오름차순으로 정렬 (숫자가 앞으로 옴)
sorted_n = sorted(n)
# 문자열에서 숫자를 제외한 문자를 제거 (정규식)
# 정확히는 re.sub(pattern, repl, string)으로 string 내에서 pattern과 일치하는 항목을 repl로 교체
number_n = re.sub(r'[^0-9]', '', n)

# 숫자의 덧셈값 초기화
result = 0

# 문자열에 속해 있던 숫자들을 더해줌과 동시에 기존 문자열에서 숫자 제거
for i in number_n:
    result += int(i)
    # 오름차순으로 정렬했을 때 숫자가 문자 앞으로 오기 때문에 숫자의 수 만큼 0 index pop()연산
    sorted_n.pop(0)

# 연산한 숫자 문자열에 append
sorted_n.append(str(result))
# ''.join() 연산을 통해 리스트를 문자열로 변환
print(''.join(sorted_n))
