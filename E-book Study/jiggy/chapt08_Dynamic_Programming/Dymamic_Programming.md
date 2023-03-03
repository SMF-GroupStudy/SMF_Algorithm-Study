다이나믹 프로그래밍
=
**다이나믹 프로그래밍(Dynamic Programming)** : 시간 및 공간 복잡도를 줄이기 위해 사용하는 알고리즘의 종류로 다음의 조건을 만족해야 사용할 수 있다.
> 1. 큰 문제를 작은 문제로 나눌 수 있다.
> 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

또한 다이나믹 프로그래밍을 사용하기 위해 자주 사용되는 메모이제이션 기법과 다이나믹 프로그래밍의 2가지 방식 탑다운과 보텀업이 존재한다.   
다음 코드는 다이나믹 프로그래밍을 사용해 피보나치 수열을 구현한 코드이다. 
~~~python
# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수(Fibonacci Funcion)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    # 종료 조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))