i, j = map(int, input().split())

# (i+j) * (i~j 까지의 개수)/2
print(((i+j) * (abs(j-i)+1))//2)