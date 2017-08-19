import sys

myInput = sys.stdin.readline
myOutput = sys.stdout.write

while True :
    kS = myInput().split()
    k = kS[0]
    if k == 0 : break

    S = kS[1:]
    maximum = k
    lottoList = S[0:6]
    changeIdx = 5

    myOutput(' '.join(lottoList)+"\n")
    while changeIdx >= 0 :
        for i in range(changeIdx+1, maximum) :
            lottoList[changeIdx] = S[i]
            myOutput(' '.join(lottoList)+"\n")
        changeIdx -= 1
        maximum -= 1
    print()