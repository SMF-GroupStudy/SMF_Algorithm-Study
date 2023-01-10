# 욕심쟁이 점원! 거스름돈의 개수를 적게해서 주고자함.
# 거스름돈을 입력 받고 최소 거름돈의 개수를 출력


#greedy 3-1 유형이랑 비슷한 문제로 그냥 바로 맞춤
change = int(input())
coin_types = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
count = 0
for coin in coin_types:
    count += change // coin
    change %= coin

print(count)
