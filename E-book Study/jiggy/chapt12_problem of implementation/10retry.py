import copy


def check(new_lock, key, n, m, x, y):
    # 맞는지 판별할 tmp 배열 생성
    # tmp_lock = new_lock
    tmp_lock = copy.deepcopy(new_lock)

    # 열쇠의 인덱스값을 하나씩 tmp 필드에 덧샘
    for i in range(m):
        for j in range(m):
            tmp_lock[x + i][y + j] += key[i][j]

    count = 0
    # 필드 가운데 위치한 자물쇠의 인덱스값 덧셈
    for i in range(n):
        for j in range(n):
            count += tmp_lock[i + n][j + n]

    # 자물쇠와 열쇠를 맞물렸을 때 인덱스값이 모두 1이라면 True return
    if count == n * n:
        return True
    else:
        return False


def solution(key, lock):
    # 열쇠와 자물쇠의 길이
    n = len(lock)
    m = len(key)

    # 처음에 2차원 배열을 아래와 같이 만들었더니 하나의 같은 열에 있는 인덱스값들이 같이 바뀜
    # frame = [[0] * len(lock[0][:]) * 3] * len(lock[:][0]) * 3

    # 열쇠를 이동하며 자물쇠와 맞추기 위한 필드
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 좌물쇠를 필드 가운데 세팅
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 필드위 열쇠가 (0, 0)에 위치하면 자물쇠와 겹치지 않기 때문에 (1, 1)부터 시작
    # 즉, x랑 y는 열쇠의 위치
    for y in range(1, n * 3):
        # 맞는 방향이 없다면 한칸씩 이동
        for x in range(1, n * 3):
            # 열쇠를 4방향으로 돌렸을 때 맞는 방향이 있는지 확인
            for _ in range(4):
                if check(new_lock, key, n, m, x, y):
                    answer = True
                    return answer
                # 열쇠 90도 회전
                key = list(zip(*key[::-1]))
    answer = False
    return answer


a = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
b = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(a, b))
