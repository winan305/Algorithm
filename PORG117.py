def digit_reverse(n):
    result = []
    for num in str(n) :
        result.append(int(num))
    result.reverse()
    return result

'''
n을 스트링으로 바꾼 후(문자 리스트가 됨) 반대로 뒤집은 결과를 리턴하는 reversed 함수를 사용, map 함수로 int형으로 바꿈
그리고 list로 변환

def digit_reverse(n):
    return list(map(int, reversed(str(n))))

스트링으로 바꾼 n을 하나씩 정수로 바꿔 리스트에 저장한 뒤 뒤집음
def digit_reverse(n):
    return [int(x) for x in str(n)][::-1]
'''
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(digit_reverse(12345)));