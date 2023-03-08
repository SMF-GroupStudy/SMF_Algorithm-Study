def check(new_lock, key, n, m, x, y):
    # 필드에 현재 열쇠의 방향과 위치에 맞게 맞물려 보기
    for i in range(m):
        for j in range(m):
            new_lock[x + i][y + j] += key[i][j]

    # 열쇠랑 자물쇠가 딱 맞물린다면 자물쇠가 위치한 부분을 다 더했을 때 n * n이 나옴
    count = 0
    for i in range(n):
        for j in range(n):
            # 맞물렸을 때 자물쇠 부분으 1이라면 (2일 경우 돌기 부분끼리 맞닿은 거임)
            if new_lock[i + n][j + n] == 1:
                count += 1

    if count == n * n:
        return True
    else:
        # 열쇠가 맞지 않았을 경우 다시 열쇠 제거 / 이 부분을 고려하지 못해서 처음에 틀림
        for i in range(m):
            for j in range(m):
                new_lock[x + i][y + j] -= key[i][j]


def solution(key, lock):
    # 자물쇠와 열쇠의 길이
    n = len(lock)
    m = len(key)

    # 자물쇠와 열쇠를 움직이며 맞물릴 수 있는 필드 생성
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 필드에 자물쇠값 입력
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # x, y는 열쇠를 1칸씩 움직여줌 이 때, 맞물리는 지점만 보기 위해 1부터 2*n 까지
    for y in range(1, n * 2):
        for x in range(1, n * 2):
            # 열쇠를 4방향으로 회전해 가며 맞물리며 이동
            for _ in range(4):
                # 돌기와 홈이 딱 맞물리는지 확인
                if check(new_lock, key, n, m, x, y):
                    # 맞물릴 경우 True
                    answer = True
                    return answer
                # 열쇠 90도 회전
                key = list(zip(*key[::-1]))
    # 위 모든 경우의 수를 돌려도 맞지 않다면 불가 False
    answer = False
    return answer
