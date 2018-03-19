# https://www.acmicpc.net/problem/1937
# 욕심쟁이 판다
# DFS, DP, LIS

import sys

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())

val = []
dp = [[0 for col in range(N)] for row in range(N)]
visit = [[False for col in range(N)] for row in range(N)]

answer = 0

for i in range(N) :
    val.append(list(map(int, read().split())))

def isValid(x, y) :
    if x < 0 or y < 0 or x >= N or y >= N : return False
    return True

def dfs(x, y) :
    global answer

    if not visit[x][y] :
        dp[x][y] = 1
        visit[x][y] = True

    off_x = [-1, 1, 0, 0]
    off_y = [0, 0, -1, 1]

    for i in range(4) :
        nextX, nextY = x + off_x[i], y + off_y[i]

        if isValid(nextX, nextY) :
            if visit[nextX][nextY]:
                dp[nextX][nextY] = max(dp[nextX][nextY], dp[x][y] + 1)

            elif val[nextX][nextY] > val[x][y] :
                dp[nextX][nextY] = max(dp[nextX][nextY], dp[x][y] + 1)
                dfs(nextX, nextY)

    answer = max(answer, dp[x][y])

for i in range(N) :
    for j in range(N) :
        if not visit[i][j] :
            dfs(i,j)
print(answer)