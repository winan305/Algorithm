def sumMatrix(A, B):
    row = col = len(A)
    answer = [[A[r][c]+B[r][c] for c in range(col)] for r in range(row)]
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))