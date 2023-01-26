n, c = map(int, input().split())
x = list(int(input()) for i in range(n))
x.sort()
result = 0
def binary_search(array, start, end):
     while start <= end:
        c_number = 1
        mid = (start + end) // 2
        share = array[0]
        for i in x:
            if i-share >= mid:
                c_number += 1
                share = i
        # Value Error 가 계속 떠가지고 뭐 때문인가 했는데 첨에
        # if c_number < c:
        #     end = mid - 1
        # else:
        #     start = mid + 1
        #     if c_number == c:  --> c_number == c가 없는 변수가 생김 그래서 Value Error가 뜰수도 있음. 그래서 밑으로 바꿈
        #         result.append(mid)
        if c_number >= c:
            global result
            start = mid + 1
            result = mid
        else:
            end = mid - 1

            ## 그리고 여기 변수에도 start를 1이라 생각안하고 최소거리가 1인데 난 시작지점으로 생각해서 0으로 잘못생각함.
binary_search(x, 1, x[n-1] - x[0])
print(result)


# Value Error 가 계속 떠가지고 뭐 때문인가 했는데 첨에