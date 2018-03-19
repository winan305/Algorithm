# https://programmers.co.kr/learn/challenge_codes/189

def findLargestSquare(board):
    answer = 0
    N = len(board)
    DP = [[0 for col in range(N)] for row in range(N)]
    offset = [[-1, 0], [0, -1], [-1, -1]]
    for i in range(N) :
        for j in range(N) :

    return answer

def check(row, col, mN) :
    if row < 0 or col < 0 : return False
    elif row >= N or col >= N : return False
    return True

#아래 코드는 출력을 위한 테스트 코드입니다.

testBoard = [['X','O','O','O','X'],['X','O','O','O','O'],['X','X','O','O','O'],['X','X','O','O','O'],['X','X','X','X','X']]
print(findLargestSquare(testBoard))