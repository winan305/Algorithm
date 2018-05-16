# 2018 SummerCoding - 여름방학 스타트업 인턴 프로그램
# 2018-04-28(토) 13:00~15:00 온라인 예선

# 문제 1
'''
# d의 길이가 작아서 시간복잡도는 크게 신경쓰지 않아도 됨.
# 값이 가장 작은 것 부터 골라야 당연히 최대가 됨.
# 값을 딱 맞출 필요도 없고 단순히 가장 많으면 되기 때문에.
# 작은 것 부터 골라가며 budget 보다 작거나 같을때 까지 반복하면 되는 문제

def solution(d, budget):
    answer = 0
    total = 0
    d.sort()

    for money in d :
        total += money

        if total <= budget :
            answer += 1
        else : break

    return answer
print(solution([1,3,2,5,4], 9))'''

# 문제 2
'''
# 단어를 순서대로 N명의 플레이어만큼 돌아감
# 단어 썼는지 안썼는지 검사
# 현재단어가 이전단어의 끝 스펠링으로 시작하는지 검사
# 플레이어 번호랑 차례가 1부터 시작인 것을 주의해야 함

def solution(n, words):
    turns = [0] * n # 플레이어들의 차례수 저장
    player = 0      # 현재 단어를 말하는 플레이어
    isUsing = {}    # 단어:사용여부(True,False) 를 저장할 딕셔너리
    length = len(words)
    
    # 딕셔너리에 단어:False 저장
    for word in words :
        isUsing[word] = False
    
    # 게임 시작
    for i in range(length) :
        turns[player] += 1
        
        # 단어 사용 여부 검사
        if isUsing[words[i]] :
            return [player+1, turns[player]]
        
        # 이전단어의 끝 스펠링과 현재단어의 처음 스펠링 검사
        elif i > 0 :
            prev_word, now_word = words[i-1], words[i]
            if prev_word[len(prev_word)-1] is not now_word[0] :
                return [player + 1, turns[player]]
        
        # 위 검사에 통과하였음, 단어 체크하고 다음 플레이어로 차례 넘김
        isUsing[words[i]] = True
        player = (player+1)%n
    # 여기까지 도달했다는 것은 아무도 패배하지 않음.
    return [0,0]

print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))'''

# 문제 3
'''
# B팀이 얻는 승점.
# 가장 큰 점수가 가장 큰 점수를 이겨야 승점이 최대가 되는 조건인 듯
# 그 외의 경우도 있지만 입력 크기가 100,000 이기 때문에 N^2로 해결 불가능하다고 판단
# 역순으로 정렬해서 B의 가장 큰 값이 이길 수 있는 A의 가장 큰 값을 찾음

def solution(A, B):
    N = len(A)
    answer = 0
    A = sorted(A, reverse=True) # 역순으로 A, B 정렬
    B = sorted(B, reverse=True)
    win_index = -1 # B가 이길 수 있는 가장 큰 점수 인덱스 저장

    for i in range(N) :
        if A[i] < B[0] :
            win_index = i
            break
            
    # 인덱스가 -1 이라는건 B가 이길 수 없음. return 0        
    if win_index == -1 :
        return 0
    
    # j는 B의 인덱스.
    j = 0
    for i in range(win_index, N) :
        # B가 A로부터 이길 수 있는 인덱스인 win_index 부터 시작
        # B가 이길 때 마다 승점을 1 증가하고 B의 인덱스를 1 증가.
        # 그래야 큰 점수가 큰 점수를 이기게 할 수 있음.
        if A[i] < B[j] :
            answer += 1
            j += 1
    # 결과 반환.
    return answer
print(solution([9,8,7,6],[8,7,6,5]))'''

# 올클리어.

