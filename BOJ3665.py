import sys
import queue

read = sys.stdin.readline
write = sys.stdout.write

T = int(read())

ANSWER_IMPOSSIBEL = 0
ANSWER_NONE = 1
ANSWER_PRINT = 2
for i in range(T) :
    N = int(read())

    graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
    indegree = [0] * (N+1)

    t = list(map(int, read().split()))

    for i in range(N) :
        for j in range(i+1, N) :
            graph[t[i]][t[j]] = 1
            indegree[t[j]] += 1

    m = int(read())

    for i in range(m) :
        a, b = map(int, read().split())

        if graph[a][b] == 1 :
            graph[a][b], graph[b][a] = 0, 1
            indegree[b] -= 1
            indegree[a] += 1

        else :
            graph[a][b], graph[b][a] = 1, 0
            indegree[a] -= 1
            indegree[b] += 1

    q = queue.Queue()
    rank = []
    flag = ANSWER_PRINT

    for i in range(1, N+1) :
        if indegree[i] == 0 : q.put(i)

    for i in range(N) :
        if q.empty() :
            flag = ANSWER_IMPOSSIBEL
            break

        if q.qsize() > 1 :
            flag = ANSWER_NONE
            break

        item = q.get()
        rank.append(str(item))

        for j in range(1, N+1) :
            if graph[item][j] == 1 :
                indegree[j] -= 1
                if indegree[j] == 0 : q.put(j)

    if flag == ANSWER_PRINT :
        write(' '.join(rank) + "\n")

    elif flag == ANSWER_NONE :
        write("?\n")

    elif flag == ANSWER_IMPOSSIBEL:
        write("IMPOSSIBEL\n")