change = [500, 100, 50, 10, 5, 1]
money = 1000 - int(input())
cnt = 0
i = 0
while money > 0 :
    cnt = cnt + money//change[i]
    money = money%change[i]
    i += 1
print(cnt)