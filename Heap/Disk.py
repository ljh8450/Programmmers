import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    heap = []
    start = -1
    while i < len(jobs):
        for j in jobs:#처리 가능한 작업 처리중으로 옮기기
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:#처리중인 작업에 대한 코드
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += now-current[1]
            i += 1
    return int(answer/len(jobs))
jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))