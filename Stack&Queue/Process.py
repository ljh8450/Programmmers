def solution(priorities, location):
    answer = 0
    data = []
    index = 0
    for i in range(len(priorities)):
        M = max(priorities)
        for j in range(i, len(priorities)):
            if M == priorities[j]:
                data.append(j)
                priorities.pop(j)
    print(data)
    return answer

priorities = [2, 1, 3, 2]
location = 2

print(solution(priorities, location))