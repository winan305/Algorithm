import sys

read = sys.stdin.readline
write = sys.stdout.write

while True :
    A, B = map(int,read().split())
    if A == 0 and B == 0 : break
    else :
        write(str(A+B)+"\n")