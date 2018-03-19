# https://programmers.co.kr/learn/challenge_codes/20

def numberOfPrime(n):
    isPrime = [True]*(n+1)
    isPrime[0]=isPrime[1]=False
    for i in range(2, n+1) :
        if not isPrime[i] : continue
        for j in range(2, n//i+1) :
            isPrime[i*j] = False
    print(isPrime)
    return isPrime.count(True)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numberOfPrime(5))