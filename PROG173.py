# https://programmers.co.kr/learn/challenge_codes/173

def checkBinary(n) :
    cnt = 0
    two = 1
    while two <= n :
        if n & two : cnt += 1
        two *= 2
    return cnt

def nextBigNumber(n):
    cnt = checkBinary(n)
    answer = n+1
    while checkBinary(answer) != cnt :
        answer += 1

    return answer

print(nextBigNumber(78))