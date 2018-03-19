# https://www.acmicpc.net/problem/1032

import sys

read = sys.stdin.readline
N = int(input())
cmds = []

for _ in range(N) :
    cmds.append(list(read()))

base = cmds[0]

for cmd in cmds:
    for j in range(len(base)):
        if base[j] == "?": continue
        if base[j] != cmd[j]:
            base[j] = "?"

print(''.join(base))
