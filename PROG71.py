# https://programmers.co.kr/learn/challenge_codes/71

import math
'''def numberBlock(begin, end):
    answer = []
    for i in range(begin, end+1) :
        answer.append(getMaxDivisor(i))
    return answer

def getMaxDivisor(number) :
    divisor = 1
    LIMIT = 10000000
    for i in range(1, int(math.sqrt(number))+1) :
        if number%i == 0 :
            if i <= LIMIT : divisor = max(divisor, i)
            if number//i <= LIMIT : divisor = max(divisor, number//i)
    return divisor
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numberBlock(99999999999990, 100000000000000))'''

# 1번 문제
'''birds = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0} # 새의 타입 딕셔너리, 1부터 5타입으로 한정, 모두 0마리로 초기화
types = list(map(int, input("숫자를입력하세요 : ").split())) # 새 타입 입력

for type in types : # 입력받은 타입(키값)들의 밸류값 1씩 증가
    birds[type] += 1

maxType = 0 # 가장 많은 타입 저장
maxBird = 0 # 가장 많은 타입의 새 마리수 저장

for type in range(1, 6) : # 1번 타입부터 5번 타입까지 반복
    if birds[type] > maxBird : # 현재 타입의 새 마리수가 저장된 최대 마리수보다 큰 경우
        maxType = type # 새로운 최대 타입 저장
        maxBird = birds[type] # 해당 타입의 최대 마리수 저장

print(maxType) # 최대 타입 출력'''
'''
# 2번 문제
couples = 0 # 양말의 짝 수 저장 변수
colors = list(map(int, input().split())) # 색상을 입력받는다.
socks = [] # 색상으로 양말들을 저장할 리스트

for color in colors : # 입력받은 색상들을 반복한다.
    if color not in socks : socks.append(color) # 현재 색상의 양말이 리스트에 없으면 추가
    else : # 리스트에 있다면 짝이 맞는 경우다.
        socks.remove(color) # 해당 색상 양말 짝 제거(리스트에 존재하는 양말만 제거하면 됨.)
        couples += 1 # 짝수 증가

print(couples) # 결과값 출력

# 3번 문제
n, m ,s = map(int, input().split()) # n, m, s 입력 후 값 저장
while m > 1 : # m(사탕)이 1이 될 때 까지 반복
    m -= 1 # 사탕을 하나 줄인다.
    s = s%n + 1 # 번호를 n(사람수)로 나눈 나머지에 1을 더해서 1,2,3,4,5,1,2,.. 로 순환
    # 사탕이 1개가 남으면 그 다음 더해진 s(죄수번호)가 결과값이 된다.

print(s) # 결과값 출력
'''

items = ["a", "b", "c"]
result = []
for i in range(len(items)) :
    for j in range(len(items)) :
        result.append(items[i] + items[j])
print(result)