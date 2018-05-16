# https://www.acmicpc.net/problem/5597
# 과제 안 내신 분..?
# 구현

students = [False] * 30

for _ in range(28) :
    number = int(input())
    students[number-1] = True

for i in range(30) :
    if not students[i] :
        print(i+1)