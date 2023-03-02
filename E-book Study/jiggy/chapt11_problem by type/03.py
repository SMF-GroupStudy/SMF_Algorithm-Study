# 0 또는 1로 구성된 문자열 입력 받기
s = input()

# 연속된 묶음 수 초기화
zero_bundle_count = 0
one_bundle_count = 0
# 반목분에서 이전 값을 저장할 변수 초기화(첫 if 문에 걸리지 않기 위해 해당 문제에 존재하지 않는 값 대입)
tmp = "2"

# 문자열 리스트를 하나씩 반복
for i in s:
    # 0이면서 이전 변수와 동일하지 않다면 묶음 수 증가
    if i == "0":
        if i == tmp:
            continue
        zero_bundle_count += 1
    # 1이면서 이전 변수와 동일하지 않다면 묶음 수 증가
    else:
        if i == tmp:
            continue
        one_bundle_count += 1
    tmp = i

# 더 작은 묶음 수 출력
if one_bundle_count >= zero_bundle_count:
    print(zero_bundle_count)
else:
    print(one_bundle_count)
