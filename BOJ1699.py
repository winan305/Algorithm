N = int(input())

LIMIT = 99999999999
DP = [LIMIT] * (N+1)

for i in range(1, N+1) :
    if (i*i) < N : DP[i*i] = 1
    j = 1
    while (i-j*j) >= 0 :
        DP[i] = min(DP[i], DP[i-j*j]+1)
        j+=1

print(DP[N])

