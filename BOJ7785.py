import sys

read = sys.stdin.readline
write = sys.stdout.write

n = int(read())
working = set()

for i in range(n) :
    name, work = read().split()
    if work == 'enter' :
        working.add(name)

    else :
        working.remove(name)

print('\n'.join(sorted(list(working), reverse=True)))