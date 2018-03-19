# https://www.acmicpc.net/problem/1904

# 짝수 : 00, 11 만 가능
# 홀수 : 1 만 가능

N = int(input())
if N < 3 : print(N)
else :
    MOD = 15746
    DP = [0] * (N+1)
    DP[1] = 1
    DP[2] = 2

    for i in range(3, N+1) :
        if i%2 == 0 :
            DP[i] = ((DP[i-2]%MOD)*2 + 1)%MOD
        else :
            DP[i] = DP[i-1]%MOD

    print(DP[N]%MOD)