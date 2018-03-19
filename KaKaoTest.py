''' 문제 1

def getBinaryList(n, length) :
    binaryList = []
    while(n >= 0 and len(binaryList) < length) :
        binaryList.append(n%2)
        n //= 2

    return binaryList

def solution(n, arr1, arr2):
    answer = [-1] * n
    binaryList1 = []
    binaryList2 = []

    for i in range(n) :
        binaryList1 = getBinaryList(arr1[i], n)
        binaryList2 = getBinaryList(arr2[i], n)
        print(binaryList1)
        print(binaryList2)
        deco = ""
        for _ in range(n) :
            item1 = binaryList1.pop()
            item2 = binaryList2.pop()
            if(item1 == 1 or item2 == 1) : deco += "#"
            elif(item1 == 0) : deco += " "
            elif(item2 == 0) : deco += " "
        answer[i] = deco

    return answer'''

'''문제 2

def solution(dartResult):
    resultList = []
    tmp = []
    i = 0
    while i < len(dartResult) :
        c = dartResult[i]
        print(i, c)
        if(c >= '0' and c <= '9') :
            if(dartResult[i+1] == '0') :
                c = c + dartResult[i + 1]
                i += 1
            resultList.append(tmp)
            tmp = []
            tmp.append(int(c))
        else :
            tmp.append(c)
        i += 1
    resultList.append(tmp)
    resultList.pop(0)
    print(resultList)

    for i in range(3) :
        for j in range(1, len(resultList[i])) :
            if resultList[i][j] == 'D' : resultList[i][0] = pow(resultList[i][0], 2)
            elif resultList[i][j] == 'T': resultList[i][0] = pow(resultList[i][0], 3)
            elif resultList[i][j] == '*' :
                resultList[i][0] *= 2
                if(i > 0) : resultList[i-1][0] *= 2
            elif resultList[i][j] == '#' : resultList[i][0] *= -1

    return resultList[0][0] + resultList[1][0] + resultList[2][0]

print(solution("1D2S#10S"))'''

'''문제 3

def solution(cacheSize, cities):
    answer = 0
    cache = []
    if(cacheSize == 0) : return 5 * len(cities)

    for city in cities :
        city = city.lower()

        if(city in cache) :
            cache.remove(city)
            cache.append(city)
            answer += 1
            continue
        else :
            if(len(cache) >= cacheSize) :
                del cache[0]
            cache.append(city)
            answer += 5
    return answer'''

def check(c) :
    if c >= 'a' and c <= 'z' : return True
    return False
def getPartList(str) :
    str = str.lower()
    result = []
    i = 0
    while i+1 < len(str) :
        if check(str[i]) and check(str[i+1]) :
            result.append(str[i] + str[i+1])
        i += 1
    return result

def solution(str1, str2):
    list1 = getPartList(str1)
    list2 = getPartList(str2)
    print(list1)
    print(list2)
    set1 = set(set(getPartList(str1)) & set(getPartList(str2)))
    set2 = set(set(getPartList(str1)) | set(getPartList(str2)))

    if len(set1) == 0 and len(set2) == 0 : return 65536
    answer = int((len(set1) / len(set2)) * 65536)
    return answer

print(solution("aa1+aa2", "AAAA12"))