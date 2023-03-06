#럭키 스트레이트
# 왼쪽 더하기 오른쪽 더하기가 같음 - 럭키스트레이트

n = input() # 항상 자릿수가 짝수 형태로만 주어짐 10~ 1억 전까지 이기때문에 O(n) 까지도 가능함. 하지만 안될수도있음.

left = 0 # 왼쪽값
right = 0 # 오른쪽 값

len_n = len(n) // 2

for i in range(len_n): # O(n)이 안되는걸 방지하고자 O(n/2)으로 함
    # 012
        left += int(n[i])
    # 345
        right += int(n[i+ len_n])

if left != right:
    print("READY")
else:
    print("LUCKY")