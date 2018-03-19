# https://programmers.co.kr/learn/challenge_codes/32

def jumpCase(num):
    if num < 3 : return num
    else :
        result = [0] * (num+1)
        result[1] = 1
        result[2] = 2
        for i in range(3, num+1) :
            result[i] = result[i-1] + result[i-2]
    return result[num]

#아래는 테스트로 출력해 보기 위한 코드입니다.
print(jumpCase(4))
