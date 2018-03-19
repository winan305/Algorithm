# https://www.acmicpc.net/problem/11656

S = list(input())
answer = []

for i in range(len(S)) :
    answer.append(S[i:])

answer.sort()

for s in answer :
    print("".join(s))

