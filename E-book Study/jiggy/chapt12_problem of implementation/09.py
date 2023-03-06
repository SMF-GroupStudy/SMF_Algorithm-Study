# 문자열 입력
s = input()

# 문자열을 몇개 단위로 나누었을 때 압축되는 문자열을 길이를 해당 리스트에 저장
length_list = [0] * ((len(s) // 2) + 1)
# 0 단위로 문자열을 나눌 수 없기 때문에 해당 인덱스 최대값으로 초기화
length_list[0] = 1000

# s의 길이의 절반보다 큰 단위는 의미 없기 때문에 절반 크기까지 반복문 실행
for i in range(1, (len(s) // 2) + 1):
    # 단위에 해당하는 list 0으로 초기화
    length_list[i] = 0
    # 연속되는 문자열의 수 초기화
    count = 1

    # 단위 만큼 인덱스 증가
    for j in range(0, len(s), i):
        # 단위 만큼 문자열 슬라이스 후 비교
        if s[j:j+i] == s[j+i:j+i+i]:
            # 연속된 단위 문자열이 같다면 count
            count += 1
        else:
            # 연속된 단위 문자열이 다르다면 반복된 수에 따라 문자열 길이 기록
            # count가 1이 아닐경우 다음 문자열을 위해 초기화
            if count == 1:
                length_list[i] += i
            else:
                if count < 10:
                    length_list[i] += 1 + i
                    count = 1
                elif count < 100:
                    length_list[i] += 2 + i
                    count = 1
                else:
                    length_list[i] += 3 + i
                    count = 1

# 리스트중 최소값 출력
print(min(length_list))
