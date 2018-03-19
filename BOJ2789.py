# https://www.acmicpc.net/problem/2789

str = input()

for c in str :
    if c in "CAMBRIDGE":
        str = str.replace(c, "")

print(str)