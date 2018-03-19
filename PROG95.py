# https://programmers.co.kr/learn/challenge_codes/95

def strange_sort(strings, n) :
    return sorted(strings, key = lambda string : string[n])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( strange_sort(["sun", "bed", "car"], 1) )
