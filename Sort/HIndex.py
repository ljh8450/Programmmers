def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
    return len(citations)

citations = [3, 0, 6, 1, 5]
print(solution(citations))