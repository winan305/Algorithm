L, P = map(int, input().split())
attendents = list(map(int, input().split()))
answers = []
for i in range(5) :
    answers.append(str(attendents[i] - L*P))
print(' '.join(answers))