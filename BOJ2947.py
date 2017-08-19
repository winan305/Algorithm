tree = list(map(int, input().split()))

for i in range(5) :
    for j in range(4) :
        if tree[j] > tree[j+1] :
            tree[j], tree[j+1] = tree[j+1], tree[j]
            print(' '.join(map(str,tree)))