import sys # sys 모듈 임포트

read = sys.stdin.readline # 입력
R, C = map(int, read().split())
offset = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 움직임 방향 리스트
board = [None] * R # 보드 생성
isUsedAlphabet = [False] * 26
move = 0 # 움직임 수 생성

for r in range(R): # 보드 입력
    board[r] = read()

def dfs(r, c, moving) :
    # 최대이동수 저장
    global move
    move = max(moving, move)
    for offsetR, offsetC in offset :
        nextR, nextC = r + offsetR, c + offsetC
        # 다음 위치가 유효하지 않은 위치거나 이미 사용한 알파벳이면 이동하지 않는다.
        if (nextR < 0 or nextC < 0 or nextR >= R or nextC >= C) : continue

        alphabet = ord(board[nextR][nextC]) - 65
        if isUsedAlphabet[alphabet] : continue

        isUsedAlphabet[alphabet] = True
        dfs(nextR, nextC, moving + 1)
        # 끝까지 탐색하면 다시 방문하지 않았음으로 표시함.
        # 다른 경로에서 탐색가능하게 한다.
        isUsedAlphabet[alphabet] = False

isUsedAlphabet[ord(board[0][0])-65] = True
dfs(0,0,1)
print(move)