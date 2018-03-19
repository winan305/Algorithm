T = int(input())

while T > 0 :
    n = int(input())
    binaryPos = []
    i = 1
    pos = 0
    while i <= n :
        if n & i : binaryPos.append(str(pos))
        i *= 2
        pos += 1

    print(' '.join(binaryPos))
    T -= 1