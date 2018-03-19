# https://www.acmicpc.net/problem/1120

def getDif(a, b):
    dif = 0
    for i in range(len(a)):
        if a[i] != b[i]: dif += 1
    return dif

A, B = input().split()

if len(A) > len(B) : A, B = B, A

answer = 9876543210
l = len(A)

for i in range(len(B) - l + 1) :
    dif = getDif(A, B[i:i+l])
    if dif < answer : answer = dif

print(answer)