# a<b 이면, a부터 b까지 더한 후 +b, 아니면 b부터 a까지 더한 후 +ㅁ
# 양수, 음수에 영향을 받지 않음.
# 이걸 내가 짯다는게 신기
def adder(a, b):
    return sum(range(a,b))+b if a<b else sum(range(b,a))+a
print( adder(3, 5))
