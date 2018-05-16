# https://www.acmicpc.net/problem/10798
# 세로 읽기

words = [None] * 5
max_len = 0
for i in range(5) :
    words[i] = input()
    max_len = max(max_len, len(words[i]))

for i in range(max_len) :
    for j in range(5) :
        if len(words[j]) > i :
            print(words[j][i], end='')