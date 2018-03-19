# https://programmers.co.kr/learn/challenge_codes/26

def noOvertime(n, works):
    for i in range(n) :
        works[works.index(max(works))] -= 1
    return sum(work**2 for work in works)

print(noOvertime(4, [4,3,3]))


