def solution(sizes):
    answer = 0
    x = [0]*len(sizes)
    y = [0]*len(sizes)
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            x[i] = sizes[i][0]
            y[i] = sizes[i][1]
        else:
            x[i] = sizes[i][1]
            y[i] = sizes[i][0]
    return max(x)*max(y)

sizes = [1,3,2,4,2]
print(solution(sizes))