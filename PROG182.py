# https://programmers.co.kr/learn/challenge_codes/182
# 최솟값 만들기

def getMinSum(A,B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for i in range(len(A)) :
        answer = answer + A[i]*B[i]

    return answer

#아래 코드는 출력을 위한 테스트 코드입니다.

print(getMinSum([1,2],[3,4]))