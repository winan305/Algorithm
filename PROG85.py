# DP 이용. LCS랑 동일한 문제.
def longest_palindrom(s):
    N = len(s)
    sr = s[::-1]
    dp = [[0 for col in range(N+1)] for row in range(N+1)]
    for i in range(1, N+1) :
        for j in range(1, N+1) :
            if s[i-1] == sr[j-1] : dp[i][j] = dp[i-1][j-1] + 1
            else : dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[N][N]

'''
def longest_palindrom(s):
    # s를 뒤집은것과 s 가 같으면 len(s) 리턴
    # 아닐경우 s의 왼쪽을 하나 자른 문자열과 오른쪽을 하나 자른 문자열을 재귀호출하여 큰 값 리턴.
    
    return len(s) if s[::-1] == s else max(longest_palindrom(s[:-1]), longest_palindrom(s[1:]))
'''
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(longest_palindrom("토마토맛토마토"))
print(longest_palindrom("토마토맛있어"))