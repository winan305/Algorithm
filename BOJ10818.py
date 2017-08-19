N = int(input())
arr = list(map(int, input().split()))

maxVal = -1000001
minVal = 1000001
for i in range(N) :
    maxVal = max(maxVal, arr[i])
    minVal = min(minVal, arr[i])

print(minVal, maxVal)