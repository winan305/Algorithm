# https://programmers.co.kr/learn/challenge_codes/143

# A = (a*b), B = (b*c) 형태여야 곱셈 가능.
# 결과는 a*c 행렬이 나옴.
def productMatrix(A, B):
    a, b, c = len(A), len(B), len(B[0])
    result = [[0 for col in range(c)] for row in range(a)]
    for i in range(a) :
        for j in range(b):
            for k in range(c):
                print(i, j, k)
                result[i][k] += A[i][j]*B[j][k]

    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 2, 3 ], [ 2, 3, 1 ]];
b = [[ 3, 4], [5, 6], [7,8]];
print("결과 : {}".format(productMatrix(a,b)))
a = [ [ 1, 2 ], [ 2, 3 ]];
b = [[ 3, 4], [5, 6]];
print("결과 : {}".format(productMatrix(a,b)));