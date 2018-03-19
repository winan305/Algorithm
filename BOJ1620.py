import sys

read = sys.stdin.readline
write = sys.stdout.write

M, N = map(int, read().split())

dict = {}

for i in range(1, M+1) :
    poc = read().strip('\n')
    dict[str(i)] = poc
    dict[poc] = str(i)

for _ in range(N) :
    print(dict[read().strip('\n')])