# https://www.acmicpc.net/problem/10815
# 숫자 카드
# 이분 탐색

N = int(input())
num_cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

num_cards.sort()
check = []

def binary_search(left, right, key) :
    if left > right : return "0"

    mid = (right+left)//2
    value = num_cards[mid]

    if value == key : return "1"
    elif value < key :
        return binary_search(mid+1, right, key)
    elif value > key :
        return binary_search(left, mid-1, key)

for num in nums :
    check.append(binary_search(0, len(num_cards)-1, num))

print(" ".join(check))

N = int(input())
num_cards = set(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

print(' '.join('1' if num in num_cards else '0' for num in nums))