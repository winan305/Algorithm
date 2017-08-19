import sys

read = sys.stdin.readline
write = sys.stdin.write

T = int(read())
print("T : ", T)
for _ in range(T) :
    n = int(read())
    print("n : ", n)
    score = [0] * 2
    DP = [[0 for col in range(n)] for row in range(2)]
    for i in range(2) :
        score[i] = list(map(int, read().split()))
    print(DP)

