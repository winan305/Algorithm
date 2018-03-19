# https://www.acmicpc.net/problem/2857

FBIs = []

for i in range(5):
    fbi = input()
    if "FBI" in fbi:
        FBIs.append(str(i+1))

if len(FBIs) > 0 :
    print(" ".join(FBIs))

else:
    print("HE GOT AWAY!")