import sys

read = sys.stdin.readline

N, M = map(int, read().split())
maze = [None] * (N)
DP = [[0 for col in range(M)] for row in range(N)]
for i in range(N) :
    maze[i] = list(map(int, read().split()))

for i in range(N) :
    for j in range(M) :
        if (i-1) >= 0 : DP[i][j] = max(DP[i-1][j] + maze[i][j], DP[i][j])
        if (j-1) >= 0 : DP[i][j] = max(DP[i][j-1] + maze[i][j], DP[i][j])
        if (i-1) >= 0 and (j-1) >= 0 : DP[i][j] = max(DP[i-1][j-1] + maze[i][j], DP[i][j])

print(DP[N-1][M-1])