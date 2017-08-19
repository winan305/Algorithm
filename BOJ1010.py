import sys

read = sys.stdin.readline
write = sys.stdout.write

def get_factorial(n) :
    factorial = 1
    for f in range(2,n+1) :
        factorial *= f
    return factorial

T = int(read())

for i in range(T) :
    N, M = map(int, read().split())
    print(get_factorial(M)//(get_factorial(N)*get_factorial(M-N)))
