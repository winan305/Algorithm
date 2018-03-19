# https://www.acmicpc.net/problem/1915
# 가장 큰 정사각형
# DP

import sys

read = sys.stdin.readline

N, M = map(int, read().split())

arr = []
dp = [[0 for col in range(M)] for row in range(N)]
answer = 0

for i in range(N) :
    tmp = []
    nums = read()
    for j in range(M) :
        tmp.append(int(nums[j]))
    arr.append(tmp)

for i in range(N) :
    for j in range(M) :
        dp[i][j] = arr[i][j]
        if i > 0 and j > 0 :
            if arr[i][j] == 1 :
                dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1

        answer = max(dp[i][j], answer)

print(answer*answer)