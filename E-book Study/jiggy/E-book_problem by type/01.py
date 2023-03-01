# 총 모험가 수 입력 1 <= N <= 100000 자연수
n = int(input())

# 모험가별 공포도 리스트
fear_list = list(map(int, input().split()))

# 모험가 공포도를 내림차순으로 정렬
fear_list.sort(reverse=True)
# 길드화할 수 있는 결과값 초기화
count_guild = 0

while True:
    # 모험가들이 전부 길드화 될 때까지 반복
    if fear_list:
        # 남은 모험가 중 최대 공포도 저장(길드 구성원 수)
        guild_member = fear_list[0]

        # 남아 있는 모험가의 최대 공포도로 길드를 구성할 수 있는지 판별 구성할 수 있다면 길드 수 +1
        if (len(fear_list) - guild_member) >= 0:
            count_guild += 1
            # 길드가 구성된 모험가는 제외
            for _ in range(guild_member):
                fear_list.pop(0)
        # 길드를 구성할 수 없다면 해당 모험가 마을에 남김
        else:
            fear_list.pop(0)
    # 모험가 공포도 리스트가 비었다면 break
    else:
        break

print(count_guild)
