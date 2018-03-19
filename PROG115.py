def toWeirdCase(s):
    s = s.split()
    result = ""
    for word in s :
        for i in range(len(word)) :
            if i%2 == 0 : result += word[i].upper()
            else : result += word[i].lower()
        result += " "
    return result.rstrip()

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")));