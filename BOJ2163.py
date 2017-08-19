N, M = map(int, input().split())

if N < M :
    N, M = M, N

DP = [0] * (N+1) # DP[i] = i * M 크기의 초콜릿을 자르는 횟수 (가로 * 세로)
DP[1] = N-1

for i in range(2, N+1) :
    DP[i] = DP[1] + DP[i-1] + 1

print(DP[M])
