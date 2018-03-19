# https://programmers.co.kr/learn/challenge_codes/88

def is_pair(s):
    brackets = []
    for c in s :
        print(brackets, c)
        if c == '(' : brackets.append('(')
        elif c == ')' :
            if len(brackets) == 0 : return False
            else :
                brackets.pop()
    return len(brackets) == 0

def is_pair(s):
    return (s.find("(")<s.find(")") and s.count("(")==s.count(")"))
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( is_pair("(hello)()"))
print( is_pair(")("))
print( is_pair("( ) ( ( () ) () )"))