# https://www.acmicpc.net/problem/1699
# 제곱수의 합
# DP
import math

N = int(input())

dp = [9876543210] * (N+1)
dp[0] = 0
for i in range(1, N+1) :
    for j in range(1, int(math.sqrt(i))+1) :
            dp[i] = min(dp[i], dp[i-(j*j)] + 1)
print(dp[N])