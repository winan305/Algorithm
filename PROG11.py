# https://programmers.co.kr/learn/challenge_codes/11

def gcdlcm(a, b):
    # a, b = min(a, b), max(a,b) 항상 b가 더 크게.
    gcd = lambda a, b : b if a == 0 else gcd(b%a, a)
    return [gcd(a,b), (a*b)//gcd(a,b)]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))
print(gcdlcm(12,3))
print(gcdlcm(4,18))
print(gcdlcm(5,37))
