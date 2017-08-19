import queue
queue = queue.Queue() # 큐 생성
N, K = map(int, input().split()) # N, K 입력
LIMIT = 100001
queue.put([N, 0]) # 큐에 [시작점, 0초] 삽입

isVisit = [False] * LIMIT

def check(position) :
    if position >= LIMIT : return False # 한계치를 넘어서면 실패 반환
    if position < 0 : return False # 위치가 0 이하가 되면 실패 반환
    return not isVisit[position] # 현재 위치를 이미 방문했는지 여부 반환(이미 방문한 경우 실패)

while not queue.empty() :
    now = queue.get() # 큐에서 현재 상태를 얻는다.
    now_pos = now[0] # 현재 위치
    now_time = now[1]  # 현재 위치까지의 시간

    isVisit[now_pos] = True  # 현재위치 방문 표시

    if now_pos == K : # 현재 위치가 도착점인 경우
        print(now_time)
        break

    if check(now_pos-1) : # 현재 위치가 유효한지 검사
        queue.put([now_pos-1, now_time+1]) # -1 위치와 현재시간+1 삽입
    if check(now_pos+1) : # 현재 위치가 유효한지 검사
        queue.put([now_pos+1, now_time+1]) # +1 위치와 현재시간+1 삽입
    if check(now_pos*2) : # 현재 위치가 유효한지 검사
        queue.put([now_pos*2, now_time+1]) # *2 위치와 현재시간+1 삽입
