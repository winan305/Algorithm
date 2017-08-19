import sys

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())

for _ in range(N) :
    AB = read()
    write(str(int(AB[0]) + int(AB[2]))+"\n")