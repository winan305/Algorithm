# https://programmers.co.kr/learn/challenge_codes/134

def Jaden_Case(s):
    s = s.split()
    for i in range(len(s)) :
        s[i] = s[i][0].upper() + s[i][1:].lower()
    return ' '.join(s)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))