# https://programmers.co.kr/learn/challenge_codes/47

def change124(n):
    answer = ""
    dict = {0: "4", 1: "1", 2: "2"}

    while n > 0:
        n, m = n//3, n%3
        if m == 0 :
            n-=1
        answer = dict[m] + answer
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(change124(3))
print(change124(4))
print(change124(5))
print(change124(6))
print(change124(7))
print(change124(8))
print(change124(9))
print(change124(10))