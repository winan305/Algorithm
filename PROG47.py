# https://programmers.co.kr/learn/challenge_codes/47

def change124(n):
    numbers = [1, 2, 4]
    count = 0
    answer = 0
    for i in range(1, n+1) :
        answer += numbers[count]
        count += 1
        if count == 3 :
            answer *= 10

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(change124(10))