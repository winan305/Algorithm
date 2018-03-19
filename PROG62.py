# https://programmers.co.kr/learn/challenge_codes/62

def change(total, coin):
    answer = 0
    # case[i] 는 i원을 거슬러줄 수 있는 경우의 수
    case = [0] * (total+1)
    case[0] = 1

    for i in range(1, total+1) :
        for c in coin :
            if i >= c :
                case[i] += case[i-c]
    print(case)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(change(5, [1, 2, 5]))
0 : 1
1 : 0+1
2 : 1+1, 2
3 : 1+1+1, 2+1
4 : 1+1+1+1, 2+1+1, 2+2
5 : 1+1+1+1, 2+1+1+1, 2+2+1, 5