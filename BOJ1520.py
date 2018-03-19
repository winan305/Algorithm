import sys

read = sys.stdin.readline

M, N = map(int, read().split())

board = []

for i in range(M) :
    board.append(list(map(int, read().split())))

# dp[i][j] = max(dp
print(board)