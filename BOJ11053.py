A = int(input())
Ai = list(map(int,input().split()))

DP = [1] * A
maxLength = 0

for i in range(0, A) :
    nowVal = Ai[i]
    for j in range(0, i) :
        if nowVal > Ai[j] :
            DP[i] = max(DP[i], DP[j]+1)
    maxLength = max(DP[i], maxLength)

print(maxLength)