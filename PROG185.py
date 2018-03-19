# https://programmers.co.kr/learn/challenge_codes/185

# 이동거리 = abs(공항좌표 - 도시좌표) * 인구수
def chooseCity(n,city):
    answer = 9876543210
    min = 9876543210
    for i in range(n) :
        dist = 0
        for j in range(n) :
            dist += (abs(city[i][0] - city[j][0]) * city[j][1])
        print(min, dist, city[i])
        if dist <= min :
            if dist == min :
                answer = min(answer, city[i][0])
            else :
                min = dist
                answer = city[i][0]

    return answer

#아래 코드는 출력을 위한 테스트 코드입니다.

print(chooseCity(4,[[1,4],[2,3],[3,5],[4,1]]))