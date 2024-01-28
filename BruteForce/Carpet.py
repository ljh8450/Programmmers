def solution(brown, yellow):
    answer = []
    listb = []
    for i in range(1, yellow+1):
        x = i
        y = (yellow/i)
        a = x+2
        b = y+2
        if 2*(a+b-2) == brown:
            answer = [a, int(b)]
    return answer

brown = 24
yellow = 24
print(solution(brown, yellow))