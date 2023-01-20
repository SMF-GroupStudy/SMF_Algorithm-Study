import sys
import heapq

# 각 보석의 무게 Mi
# 각 보석의 가격 Vi
# 가방 k개
# 가방에 담을 수 있는 최대 무게 Ci 가방에는 최대 한개의 보석만 넣기가능

# n, k = map(int, input().split())
# jewel = []
# for i in range(n):
#     jewel.append(list(map(int, input().split())))
# c = []
# for i in range(k):
#     c.append(int(input()))
#
#
# def setting(price):
#     return price[1]
#
#
# jewel = sorted(jewel, key=setting, reverse=True)
# c.sort(reverse=True)
#
# result = []
#
# for i in range(n):
#     for j in range(k):
#         if jewel[i][0] <= c[j]:
#             result.append(jewel[i][1])
#             if len(result) == len(c):
#                 print(sum(result))
#             break

input = sys.stdin.readline

n,k = map(int, input().split())
gem = [list(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
gem.sort()
bag.sort()

print(gem)  # 무게순으로 정렬됨.
print(bag)

Q= []
answer = 0
for i in bag:
    while gem and gem[0][0] <= i: # 보석이 존재하고, 가방이 담을 수 있는 무게가 보석의 무게와 같거나 클때
        heapq.heappush(Q, -heapq.heappop(gem)[1]) # Q에 보석 가격을 입력 # -를 붙여 max heap을 구현
    if Q: answer -= heapq.heappop(Q)
print(answer)
