# https://www.acmicpc.net/problem/1919

word1 = input()
word2 = input()

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cnt = 0
for alphabet in alphabets:
   cnt += abs(word1.count(alphabet) - word2.count(alphabet))

print(cnt)


