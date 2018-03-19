# A * Days - B* (Days-1) >= V
# A*d - B*d + B >= v
# day(a-b) >= v+b
# day = >= (v-b)/(a-b)

A, B, V = map(int, input().split())
day = (V-B)/(A-B)
if int(day) < day : print(int(day+1))
else : print(int(day))
