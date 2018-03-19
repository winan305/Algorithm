# https://programmers.co.kr/learn/challenge_codes/2

def sumDivisor(num):
    answer = 1
    for i in range(2, num+1) :
        if num%i == 0 : answer += i
    return answer

'''
이렇게 하고싶었으나 못한 코드
def sumDivisor(num):
    return sum([i for i in range(1, num+1) if num % i == 0])
'''

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumDivisor(12))
print(sumDivisor(25)) # 1 5 25