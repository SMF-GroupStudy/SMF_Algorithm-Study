#럭키 스트레이트
# 왼쪽 더하기 오른쪽 더하기가 같음 - 럭키스트레이트

n = input() # 항상 자릿수가 짝수 형태로만 주어짐 10~ 1억 전까지 이기때문에 O(n) 까지도 가능함.

left = 0 # 왼쪽값
right = 0 # 오른쪽 값

for i in range(len(n)):
    # 012
    if i < len(n)/2: # n의 길이의 반
        left += i
    # 345
    else:
        right += 1

if left != right:
    print("READY")
else:
    print("LUCKY")