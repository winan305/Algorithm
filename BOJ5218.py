# https://www.acmicpc.net/problem/5218

import sys

read = sys.stdin.readline
write = sys.stdout.write

def printDistance(word1, word2):
    dis = []
    for i in range(len(word1)):
        x, y = ord(word1[i]), ord(word2[i])
        if y >= x: dis.append(str(y-x))
        else: dis.append(str((y+26)-x))

    write("Distances: " + " ".join(dis) +"\n")

N = int(read())
for i in range(N):
    words = read().split()
    printDistance(list(words[0]), list(words[1]))
