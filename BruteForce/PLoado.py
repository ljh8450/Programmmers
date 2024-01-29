from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons, len(dungeons)):
        temp = k
        count = 0
        for need, spend in p:
            if temp >= need:
                count += 1
                temp -= spend
        answer = max(answer, count)
    return answer

k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k, dungeons))