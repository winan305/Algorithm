# https://www.acmicpc.net/problem/5598

str = list(input())

for i in range(len(str)):
    asc = ord(str[i]) - 3
    if asc < ord('A'):
        asc += 26
    str[i] = chr(asc)

print("".join(str))

