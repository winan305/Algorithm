import sys

myInput = sys.stdin.readline

N = int(input())
for i in range(N) :
    a, b = map(int, myInput().split())
    print(a+b)