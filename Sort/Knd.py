def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        data = []
        x = commands[i][0]-1
        y = commands[i][1]
        z = commands[i][2]
        data = sorted(array[x:y])
        answer.append(data[z-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))