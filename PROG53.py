# https://programmers.co.kr/learn/challenge_codes/53

def tiling(n):
    if n < 3 : return n
    DP = [0] * (n+1)
    DP[1], DP[2] = 1, 2
    for i in range(3, n+1) :
        DP[i] = DP[i-1] + DP[i-2]
    return int(str(DP[n])[-5:])


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(tiling(30))
