# 캐릭터 점수 N
n = int(input())

# 캐릭터 점수의 자릿수 절반
half = int(len(str(n)) / 2)

# 캐릭터의 점수를 자릿수를 기준으로 절반 나누었을 때 왼쪽 오른쪽 수
left = n // (10 ** half)
right = n % (10 ** half)

# 각 자릿수의 합 초기회
left_sum, right_sum = 0, 0

# 나뉜 숫자의 각 자릿수 덧셈
for _ in range(half):
    left_sum += left % 10
    left //= 10
    right_sum += right % 10
    right //= 10

# 결과 출력
if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
