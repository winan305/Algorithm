def sort_dictionary(dic):
    key_list = list(dic.keys())
    key_list.sort()
    result = []
    for item in key_list :
        result.append((item, dic[item]))
    return result

# sorted(정렬대상, 정렬기준)
# dic.items()로 키:값 쌍을 튜플로 얻어온 뒤 x[0](=키)를 이용해 정렬 후 반환.
'''
def sort_dictionary(dic):
    return sorted(dic.items(), key=lambda x :x[0])
'''

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( sort_dictionary( {"김철수":78, "이하나":97, "정진원":88} ))