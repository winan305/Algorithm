import sys

myInput = sys.stdin.readline
myOutput = sys.stdout.write

N = int(input())

for _ in range(N) :
    candys, siblings = map(int, myInput().split())
    you = candys // siblings
    dad = candys % siblings
    myOutput("You get "+str(you)+" piece(s) and your dad gets "+str(dad)+" piece(s).\n")
