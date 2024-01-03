import math
def solution(progresses, speeds):
    answer = []
    arr = [0 for _ in range(len(progresses))] #to save how long take the task
    for i in range(len(progresses)):
        arr[i] = math.ceil((100-progresses[i])/speeds[i])
    temp = arr[0]
    x = 1
    index = 0 #if index and j are same, do not excute code
    for j in range(len(progresses)): #if following necessary period of task isn't bigger than previous task, just raise counter
        if temp >= arr[j]:
            if index == j:
                continue
            else:
                x += 1 
        else:
            if index == j:
                continue
            else: #The code of Flag. Reset numbers(temp, counter, index)
                answer.append(x)
                temp = arr[j]
                x = 1
                index = j
    if sum(answer) != len(progresses): #add last counter
        answer.append(len(progresses)-sum(answer))
    return answer