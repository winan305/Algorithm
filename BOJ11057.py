def sum1ToN(N) :
    return (N%10007*((N+1)%10007)//2)%10007

N = int(input())

DP = [0] * N

DP[0] = 10


