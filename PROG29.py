# https://programmers.co.kr/learn/challenge_codes/29

from math import gcd

def lcm(a, b):
    return a*b//gcd(a,b)

def nlcm(num):
    answer = lcm(num[0], num[1])
    for i in range(2, len(num)) :
        answer = lcm(answer, num[i])
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2,6,8,14]));