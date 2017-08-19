S = input()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

find = [-1] * 26

for i in range(26) :
    try :
        find[i] = S.index(alphabet[i])
    except ValueError :
        pass

print(' '.join(map(str, find)))
