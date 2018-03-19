# https://www.acmicpc.net/problem/6359
# 만취한 상범
# 왜 DP일까

import sys

read = sys.stdin.readline
write = sys.stdout.write

T = int(read())

for _ in range(T) :
    n = int(read())
    room = [False] * (n+1)

    for i in range(1, n+1) :
        for j in range(i, n+1, i) :
            room[j] = not room[j]

    write(str(room.count(True)) +"\n")