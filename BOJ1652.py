# https://www.acmicpc.net/problem/1652

N = int(input())
room = [None] * N

for i in range(N) :
    room[i] = input()

row, col = 0, 0

for i in range(N) :
    str = room[i].split('X')
    for s in str :
        if len(s) >= 2 : row+=1

room_c = []

for j in range(N) :
    str = ''
    for i in range(N) :
        str += room[i][j]
    room_c.append(str)

for i in range(N) :
    str = room_c[i].split('X')
    for s in str :
        if len(s) >= 2 : col+=1

print(row, col)