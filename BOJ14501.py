# https://www.acmicpc.net/problem/14501
# 퇴사
# DP

import sys

read = sys.stdin.readline

N = int(read())

T = [0] * (N+1)
P = [0] * (N+1)
DP = [0] * (N+1) # DP[i] = DP[i-1]까지 가장 큰 이득 + P[i] , i는 1일 2일 3일 ...

answer = 0
for i in range(1, N+1) :
    T[i], P[i] = map(int, read().split())

for i in range(1, N+1) :
    if T[i] + i > N+1 :
        continue

    for j in range(0, i) :
        if j+T[j] > i : continue
        DP[i] = max(DP[i], DP[j] + P[i])
        answer = max(answer, DP[i])

print(answer)