N = int(input())

DP = [0] * 31
DP[2] = 3
n = 4
while n <= N :
    DP[n] = DP[2]*DP[n-2]
    n += 2

print(DP[N])