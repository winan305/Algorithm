'''import sys

read = sys.stdin.readline
write = sys.stdout.write

LIMIT = 9876543210

T = int(read())

for _ in range(T) :
    K = int(read())
    sizes = list(map(int, read().split()))

    DP = [[LIMIT for col in range(K+1)] for row in range(K+1)]
    sum = [0] * (K+1)

    for i in range(1, K+1) : sum[i] = sum[i-1] + sizes[i]
    print(DP)


    for i in range(1, K) :
        for j in range(0, K) :
            for k in range(j, K) :
                DP[j][j+i] = min(DP[j][j+1], DP[j][k] + sizes[k+1])'''





'''
40 30 30 50
   70 60 80
   70+80+150
DP[i][j] = i번째 파일부터 j번째 파일까지 합의 최소비용
DP[0][1] = DP[0][0] + DP[1][1]
DP[1][2] = DP[1][1] + DP[2][2]
DP[2][3] = DP[2][2] + DP[3][3]
DP[0][2] = DP[0][1] + DP[2][2], DP[1][2] + DP[0][0]
DP[1][3] = DP[1][2] + DP[3][3], DP[2][3] + DP[1][1]
DP[0][3] = DP[0][2] + DP[3][3], DP[1][3] + DP[0][0] DP[ 0,1,2,3

siezs[0]+sizes[1](70), sizes[2]+sizes[3](80) + 150
'''
abc = 1
count = [0] * 10

for n in range(3) :
    abc *= int(input())

for c in str(abc) :
    count[int(c)]+=1

for i in range(10) :
    print(count[i])