# https://www.acmicpc.net/problem/1075

def getBase(n) :
    return n%10000 - n%100

N = int(input())
F = int(input())

quotient = N//F

N = quotient * F if getBase(quotient * F) == getBase(N) else (quotient+1) * F
n = N

while getBase(N) == getBase(n) :
    N = n
    n = n-F

print(str(N%100) if N%100 > 9 else "0" + str(N%100))