# https://www.acmicpc.net/problem/1003

import sys

read = sys.stdin.readline
write = sys.stdout.write

T = int(read())

dp = [None] * 41
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 41) :
    dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]

for t in range(T) :
    N = int(read())
    write(str(dp[N][0]) + ' ' + str(dp[N][1]) +"\n")