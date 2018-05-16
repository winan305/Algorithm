# https://www.acmicpc.net/problem/2960
# 에라토스테네스의 체

N, K = map(int, input().split())

def solve(N, K) :
    removed = []
    is_checked = [False] * (N + 1)
    for i in range(2, N+1) :
        if not is_checked[i] :
            j = 1
            while i*j <= N :
                if not is_checked[i*j] :
                    removed.append(i*j)
                    is_checked[i*j] = True
                j+=1
        if len(removed) >= K :
            break
    return removed[K-1]

print(solve(N,K))

