# https://www.acmicpc.net/problem/2606

import sys
import queue

write = sys.stdout.write
read = sys.stdin.readline

computers = int(read())
couples = int(read())

network = [[False for col in range(0, computers+1)] for row in range(0, computers+1)]
isVisit = [False] * (computers+1)
for _ in range(couples) :
    i, j = map(int, read().split())
    network[i][j] = network[j][i] = True

answer = 0
queue = queue.Queue()

for i in range(2, computers+1) :
    if(network[1][i]) :
        answer += 1
        queue.put([1,i])
        isVisit[i] = True

while not queue.empty() :
    now = queue.get()
    start, end = now[0], now[1]

    for i in range(2, computers+1) :
        if network[end][i] and not isVisit[i]:
            answer += 1
            queue.put([end, i])
            isVisit[i] = True

print(answer)