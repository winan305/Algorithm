# https://www.acmicpc.net/problem/2583
# 영역 구하기
# DFS 로 풀었는데 런타임에러뜸
# 같은 코드를 자바로 옮겼더니 통과됨.

import sys
read = sys.stdin.readline
M, N, K = map(int, read().split())

grid = [[False for col in range(N)] for row in range(M)]
is_visit = [[False for col in range(N)] for row in range(M)]
areas = []
area = 0
for k in range(K) :
    x1, y1, x2, y2 = map(int, read().split())
    # (x1, y1) : ( x2, y2)
    for x in range(x1, x2) :
        for y in range(y1, y2) :
            grid[y][x] = True
            is_visit[y][x] = True

def is_valid(x, y) :
    global N, M, is_visit
    if x < 0 or y < 0 or x >= N or y >= M :
        return False

    if is_visit[y][x] :
        return False

    return True

def dfs(x, y) :
    if not is_valid(x,y) :
        return

    global area, is_visit
    area += 1
    is_visit[y][x] = True
    off_x = [1, -1, 0, 0]
    off_y = [0, 0, 1, -1]

    for i in range(4) :
        dfs(x+off_x[i], y+off_y[i])

for i in range(M) :
    for j in range(N) :
        if not is_visit[i][j]:
            dfs(j,i)
            if area is not 0 :
                areas.append(area)
                area = 0

areas.sort()
print(len(areas))
print(' '.join(str(area) for area in areas))


