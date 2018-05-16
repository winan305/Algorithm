# https://www.acmicpc.net/problem/11060
# 점프 점프
# DP

N = int(input())
maze = list(map(int, input().split()))
LIMIT = 9876543210
DP = [LIMIT] * N # DP[i] 는 i번째 돌을 밟기 위해 필요한 최소의 점프 수
DP[0] = 0
for i in range(N) :
    for j in range(1, maze[i]+1) :
        if i+j < N :
            DP[i+j] = min(DP[i+j], DP[i]+1)

print(DP[N-1] if DP[N-1] is not LIMIT else -1)
