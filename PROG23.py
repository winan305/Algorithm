# https://programmers.co.kr/learn/challenge_codes/23
def caesar(s, n):
    s = s.split()
    for i in range(len(s)) :
        s[i] = chr(ord(s[i])+n)
    return ' '.join(s)
    # 주어진 문장을 암호화하여 반환하세요.


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))