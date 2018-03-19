# https://programmers.co.kr/learn/challenge_codes/41

def expressions(num):
    answer = 0

    for i in range(1, num+1) :
        sum = i
        j = i+1
        while sum < num :
            sum += j
            j += 1
        if sum == num : answer += 1

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(expressions(15));
print(expressions(8));
print(expressions(4));
