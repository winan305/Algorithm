import sys

read = sys.stdin.readline
write = sys.stdout.write

N, M = map(int, read().split())
arr = list(map(int, read().split()))
for i in range(1,N) :
    arr[i] += arr[i-1]

for _ in range(M) :
    i, j = map(int, read().split())
    i -= 2
    j -= 1
    if i < 0 : write(str(arr[j])+"\n")
    else : write(str(arr[j] - arr[i])+"\n")
