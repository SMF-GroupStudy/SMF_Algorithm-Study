
# 기둥은 바닥 위에 있거나 다른 기둥 위에 있어야 함. 보의 한 쪽 끝 부분 위에 있거나
# 보는 한쪽 끝 부분이 기둥 위에 있거나 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야함.
def possible(answer):
    for x, y, a in answer:
        if a == 0: # 기둥인 경우
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False # 아니라면 거짓 반환
        elif a == 1: # 보인 경우
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y,1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 0:
            answer.remove([x,y,a])
            if not possible(answer):
                answer.append([x,y,a])
        if b == 1:
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x,y,a])
    return sorted(answer)
