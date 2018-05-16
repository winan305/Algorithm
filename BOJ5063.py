# https://www.acmicpc.net/problem/5063
# TGN
# 구현

import sys

read = sys.stdin.readline
write = sys.stdout.write
N = int(read())
for _ in range(N) :
    r, e, c = map(int, read().split())

    rp = e-c

    if r < rp : write("advertise\n")
    elif r is rp : write("does not matter\n")
    elif r > rp : write("do not advertise\n")