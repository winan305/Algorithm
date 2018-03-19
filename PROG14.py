# https://programmers.co.kr/learn/challenge_codes/14

def collatz(num):
    answer = 0
    while num > 1 and answer < 500 :
        print(num)
        if num%2 == 0 : num//=2
        else : num = num*3+1
        answer += 1
    return answer if answer < 500 else -1

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(1000000000000000000))