import sys

read = sys.stdin.readline
write = sys.stdin.write

LIMIT = 999999999999
n, k = map(int, read().split())
value = [0] * (n)
DP = [LIMIT] * (10001)

for v in range(n) :
    value[v] = int(read())
    if value[v] < 10001 :
        DP[value[v]] = 1

for i in range(k+1) :
    for v in value :
        if i >= v :
            DP[i] = min(DP[i], DP[i-v] + DP[v])

if DP[k] == LIMIT : print(-1)
else : print(DP[k])
