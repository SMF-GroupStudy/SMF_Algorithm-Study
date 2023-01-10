# 현재 온도와 목표 온도 입력받기
a, b = map(int, input().split())  # 53 4
# 에어컨 조절 가능 온도 리스트 만들기
button = [10, 5, 1]
# 결과값 초기화
result = 0
# a와 b의 차의 절댓값을 저장
ondo = abs(a - b) # 49
for i in button:
		result += ondo // i # 49 // 10 = 4
		ondo = ondo % i # ondo = 9
		if(i != 1):
			if(i-ondo >=1 and i - ondo <=2): # 1 234 5 6789 10
				result += 1
				ondo = i- ondo

print(result)