def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
    
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    return n-len(lost)
n = 5
lost = [2, 4]
reserve = [1, 3, 5]

print(solution(n, lost, reserve))