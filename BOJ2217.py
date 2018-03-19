# https://www.acmicpc.net/problem/2217
# 로프
# 그리디

import sys

read = sys.stdin.readline

N = int(read())

W = []
for i in range(N) :
    W.append(int(read()))

W.sort(reverse=True)

answer = W[0]

nums = 2
for i in range(1, N) :
    answer = max(answer, W[i]*nums)
    nums += 1

print(answer)