# https://programmers.co.kr/learn/challenge_codes/131

def Harshad(n):
    sum = 0
    nn = n
    while nn > 0 :
        sum+=nn%10
        nn//=10

    return n%sum == 0

# 수를 String 으로 만들어 한자리씩 접근해서 int형으로 치환후 더함.
# 자릿수를 더하는 방법에 String을 활용하자.
def Harshad(n):
    return n % sum(int(x) for x in str(n)) == 0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))
