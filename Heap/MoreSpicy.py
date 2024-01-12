import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    while heap[0] < k:
        answer += 1
        heapq.heappush(heap, heapq.heappop(heap)+heapq.heappop(heap)*2)
        if len(heap) == 1 and heap[0] < k:
            return -1
    return answer

scoville = [1, 2, 3, 9, 10, 12]	
k = 7
print(solution(scoville, k))