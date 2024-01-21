def solution(numbers):
    answer = ''
    data = sorted(numbers, key = lambda x: -int(str(x)[0]))
    answer
    for i in data:
        answer = answer + str(i)
    return answer
numbers = [6, 10, 2]
print(solution(numbers))
