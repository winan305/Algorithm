# https://www.acmicpc.net/problem/5586

str = input()

# count 함수가 IOIIOI 같은 경우를 체크하지 않아서 I -> II로 바꿔줌.
str = str.replace("I", "II")
print(str.count("JOI"))
print(str.count("IOI"))