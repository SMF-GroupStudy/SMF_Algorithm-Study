# 문자열 압축

#문자열 입력
s = input()

def solution(s):
    answer = 0

    count = []
    result = [[] for _ in range(len(s))]
    a = 1 # result 인덱스
    kor = 0 # 1개씩 2개씩 3개씩 끊기 위한 끊기 변수
    num = 1 # 누적 개수

    while a < len(s):
        # result 라는 리스트에 개수 별로 끊어서 저장
        for i in range(0, len(s)):
            if kor < len(s):
                result[a].append(s[kor: kor + a])
                if i > 0 and result[a][i-1] == result[a][i]:
                    result[a][i - 1] = "" # 중복이면 ''로 비워둠
            else:
                break
            kor = kor + a
        # result 리스트에 ''가 있다는 것은 중복이 있었다는 것으로 num + 1
        for i in range(len(result[a])):
            if result[a][i] == '':
                num += 1
                result[a][i] = str(num)
                if result[a][i-1] == str(num-1): # 2a2b23c 이런식으로 23c가 나오기때문에 전에 숫자이면 없애기
                    result[a][i-1] = ''
            else:
                num = 1

        aaa = ''.join(st for st in result[a])
        count.append(len(aaa))


        kor = 0
        a += 1
        answer = min(count)
    return answer

print(solution(s))