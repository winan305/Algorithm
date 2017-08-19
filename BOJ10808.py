S = input()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count = [0]*26

for i in range(26) :
    for j in range(len(S)) :
        if S[j] == alphabet[i] : count[i] += 1
print(' '.join(map(str, count)))