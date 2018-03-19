# https://www.acmicpc.net/problem/2998

print(oct(int(input(), 2))[2:])

# int(input(), 2) -> input() 으로 입력된 문자열이 2진수이고, 이를 10진수 형태의 정수로 바꾼다.
# oct() 에 의해 10진수 정수가 8진수 형태로 바뀐다.(o0~)
# [2:] 로 인해 o0 이후의 숫자 부분만 출력하게 된다.