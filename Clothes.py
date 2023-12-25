def solution(clothes):
    hash_map = {}
    for _, t in clothes:
        if t not in hash_map:
            hash_map[t] = 2
        else:
            hash_map[t] += 1
    answer = 1
    for i in hash_map.values():
        answer *= i
    return answer-1