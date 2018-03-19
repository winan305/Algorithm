# https://www.acmicpc.net/problem/1890
# 점프
# DP

import sys

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())
board = []
# board[i][j] = v
# board[i+v][j] += 1, board[i][j+v] += 1

dp = [[0 for col in range(N)] for row in range(N)]
for _ in range(N) :
    board.append(list(map(int, read().split())))

'''def dfs(i, j) :
    dp[i][j] += 1
    v = board[i][j]
    if v == 0 : return

    if dp[i][j] != 0 :
        pass
    if i+v < N :
        dfs(i+v, j)

    if j+v < N:
        dfs(i, j+v)'''

#dfs(0,0)

dp[0][0] = 1
for i in range(N) :
    for j in range(N) :
        v = board[i][j]

        if v == 0 : continue

        if j+v < N : dp[i][j+v] += dp[i][j]
        if i+v < N : dp[i+v][j] += dp[i][j]

print(dp[N-1][N-1])

