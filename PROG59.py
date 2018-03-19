# https://programmers.co.kr/learn/challenge_codes/59

def eatCookie(cookies):
    answer = 0
    #DP[i] = i번째 쿠키를 먹을 때 까지의 최대 개수
    N = len(cookies)
    DP = [1] * N
    for i in range(1, N) :
        for j in range(i) :
            if cookies[j] < cookies[i] :
                DP[i] = max(DP[i], DP[j]+1)
    return max(DP)



# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(eatCookie([1, 4, 2, 6, 3, 4, 1, 5]))
