N = int(input())
students = list(map(int,input().split()))
ans = 0
for number in range(N) :
    if students[number] != number+1 : ans += 1

print(ans)
