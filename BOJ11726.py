n = int(input())

if n <= 2 :
    print(n)

else :
    DP = [0] * (n + 1)
    DP[1] = 1
    DP[2] = 2
    for i in range(3, n+1) :
        DP[i] = (DP[i-1] + DP[i-2])%10007
    print(DP[n])

