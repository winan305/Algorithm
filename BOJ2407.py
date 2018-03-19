# https://www.acmicpc.net/problem/2407

N, M = map(int, input().split())

def combination(N, M) :
    de, nu = 1, 1
    M = min(M, N-M)
    for i in range(M) :
        de = de * (N-i)
        nu = nu * (i+1)
    return de // nu

nCm = combination(N, M)
print(nCm)

# 5C3 = 5*4*3 / 3*2*1