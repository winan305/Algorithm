# https://www.acmicpc.net/problem/11003
# 슬라이딩 윈도우, 최소값 찾기

N, L = map(int, input().split())
Ai = list(map(int, input().split()))

i = 0
start = i - L + 1
end = i

mins = []

while end < N :
    if start < 0 : start = 0

    mins.append(str(min(Ai[start:end+1])))

    i += 1
    start = i - L + 1
    end = i

print(' '.join(mins))