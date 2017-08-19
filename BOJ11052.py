N = int(input())
P = [0] + list(map(int, input().split()))

DP = [0] * (N+1)

for i in range(1, N+1) : # i는 현재 판매할 개수
    for j in range(1, i+1) : # j는 현재의 세트
        DP[i] = max(DP[i], DP[i-j] + P[j]) # 현재 저장된 값과
                                           # j개의 세트를 판매한 값 + i-j 개를 판매한 값의 합 중 큰 값을 선택
print(DP[N])