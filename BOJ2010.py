'''import sys

read = sys.stdin.readline

N = int(read())
plugs = 0
for i in range(N) :
    plugs += int(read())

print(plugs - (N-1))'''

list_data = ["a","a", "b", "c"]
result = []
for i in range(len(list_data)):
    for j in range(len(list_data)):
        data = list_data[i] + list_data[j]
        if result.count(data) == 0:
            result.append(data)
print (result)

