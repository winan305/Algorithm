A, B = input().split()
print(int(A.replace("6", "5", A.count("6"))) + int(B.replace("6", "5", B.count("6"))), int(A.replace("5", "6", A.count("5"))) + int(B.replace("5", "6", B.count("5"))))

# 10828, 10845
# 1991(트리 클래스 구현)