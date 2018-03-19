# https://www.acmicpc.net/problem/9933

import sys

read = sys.stdin.readline
N = int(read().replace("\n", ""))

texts = []
for i in range(N) :
    texts.append(read().replace("\n", ""))

password = ""

if N == 1: password = texts[0]
else:
    for text in texts :
        if text[::-1] in texts:
            password = text
            break

print(len(password), password[(len(password)//2)])