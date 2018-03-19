# https://www.acmicpc.net/problem/1100

SIZE = 8
answer = 0
map = []

for i in range(SIZE) :
    map.append(input())
    for j in range(SIZE) :
        if i%2 == 0:
            if j%2 == 0 and map[i][j] == 'F':
                answer += 1
        else:
            if not j%2 == 0 and map[i][j] == 'F':
                answer += 1

print(answer)