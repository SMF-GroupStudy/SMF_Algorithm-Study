def solution(food_times, k):
    # 초기 시간 설정
    t = 0
    # 회전판에 놓인 음식 수
    now = 0

    while True:
        # 현재 음식 번호
        if now == 3:
            now = 0
        # 네트워크 장애 시간이 되면 break
        if t == k:
            return now + 1
        # 다 먹은 음식 번호면 continue
        if food_times[now] == 0:
            now += 1
            continue
        food_times[now] = food_times[now] - 1
        now += 1
        t += 1


print(solution([3, 1, 2], 5))
