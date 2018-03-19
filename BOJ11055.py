N = int(input())
A = list(map(int, input().split()))
DP = [a for a in A]

answer = DP[0]

for i in range(1, N) :
    for j in range(0, i) :
        if A[i] > A[j] :
            DP[i] = max(DP[i], DP[j] + A[i])

print(max(DP))