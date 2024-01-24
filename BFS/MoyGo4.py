def solution(answers):
    answer = []
    df = [1, 2, 3, 4, 5] * (len(answers)//5 + 1)
    ds = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//8 + 1)
    dt = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//10 + 1)
    one, two, thr = 0, 0, 0
    for i in range(len(answers)):
        if df[i] == answers[i]:
            one += 1
        if ds[i] == answers[i]:
            two += 1
        if dt[i] == answers[i]:
            thr += 1
    M = max(one, two, thr)
    if one == M:
        answer.append(1)
    if two == M:
        answer.append(2)
    if thr == M:
        answer.append(3)
    return answer

answers = [1,3,2,4,2]	
print(solution(answers))