import sys

read = sys.stdin.readline
write = sys.stdout.write

res = set([])

for _ in range(10) :
    res.add(int(read())%42)

print(len(list(res)))