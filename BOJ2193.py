N = int(input())

DP = [0] * 90
DP[0] = DP[1] = 1

for i in range(2,N) :
    DP[i] = DP[i-1] + DP[i-2]

print(DP[N-1])