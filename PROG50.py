# https://programmers.co.kr/learn/challenge_codes/50


#시간초과남. BFS 방식으로 풀음.
import queue

'''def setAlign(n, k):
    peoples = []
    q = queue.Queue()
    cnt = 0
    for i in range(1, n+1) :
        peoples.append(i)
        q.put([i])
    while True :
        now = q.get()
        if len(now) == n :
            cnt+=1
        if cnt == k : return now
        for i in range(n):
            if peoples[i] not in now :
                q.put(now + [peoples[i]])

    return answer
'''

def setAlign(n, k):
    answer = []
    isUsed = [False] * (n + 1)
    factorials = [1]
    for i in range(1, n+1) : factorials.append(factorials[i-1] * i)
    print(factorials)

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(setAlign(3, 5))
