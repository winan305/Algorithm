# https://www.acmicpc.net/problem/2667

import sys
import queue

write = sys.stdout.write
read = sys.stdin.readline

N = int(read())
map = [[0 for col in range(N)] for row in range(N)]
offset_x = [1, -1, 0, 0]
offset_y = [0, 0, 1, -1]

houses = []

for i in range(N) :
    nums = read()
    for j in range(N) :
        map[i][j] = int(nums[j])

def isValid(x, y) :
    if x < 0 or y < 0 or x >= N or y >= N : return False
    if map[x][y] == 0 : return False
    return True

def dfs(x, y, n) :
    houses[n] += 1
    map[x][y] = 0
    for i in range(4) :
        if isValid(x+offset_x[i], y+offset_y[i]) :
            return dfs(x+offset_x[i], y+offset_y[i], n)

n = 0
for i in range(N) :
    for j in range(N) :
        if map[i][j] == 1 :
            houses.append(0)
            dfs(i,j, n)
            n += 1

print(len(houses))
for house in houses :
    print(house)
