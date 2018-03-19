
def facto(n) :
    if n == 0 or n == 1 : return 1

    fact = 1
    for f in range(2, n+1) :
        fact = ((fact%10007) * f)%10007

    return fact%10007

N, K = map(int, input().split())

up = facto(N)%10007
down = ((facto(K)%10007) * (facto(N-K)%10007))%10007
print(up//down)

