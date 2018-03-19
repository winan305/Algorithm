# https://www.acmicpc.net/problem/9507
# Generations of Tribbles
# DP

'''import sys

read = sys.stdin.readline
MAX = 68
fibo = [0] * MAX
fibo[0], fibo[1], fibo[2], fibo[3] = 1,1,2,4

for i in range(4, MAX) :
    for j in range(1, 5) :
        fibo[i] += fibo[i-j]

T = int(input())
answer = []
for t in range(T) :
    answer.append(str(fibo[int(read())]))

print("\n".join(answer))'''
