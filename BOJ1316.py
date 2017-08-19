import sys

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())
count = N
for _ in range(N) :
    check = [False] * 26
    word = read()
    buffer = word[0]
    for i in range(1, len(word)) :
        if check[ord(buffer)-97] :
            count -= 1
            break
        if buffer == word[i] : continue
        else :
            check[ord(buffer)-97] = True
            buffer = word[i]
print(count)