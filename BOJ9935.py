# https://www.acmicpc.net/problem/9935

import sys

read = sys.stdin.readlint
write = sys.stdout.write

N = int(read())
for i in range(N) :
    str = read().split()
    str0, str1 = str[0], str[1]

print(str, str0, str1)