x = int(input())
dp = [-1] * (x + 1)

if x >= 3:
    dp[3] = 1
if x >= 5:
    dp[5] = 1

for i in range(6, x + 1):
    if dp[i - 3] < 0 and dp[i - 5] < 0:
        dp[i] = -1

    elif dp[i - 3] > 0 and dp[i - 5] > 0:
        dp[i] = 1 + min(dp[i - 3], dp[i - 5])

    else:
        dp[i] = 1 + max(dp[i - 3], dp[i - 5])

print(dp[x])
