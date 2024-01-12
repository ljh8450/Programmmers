import heapq
def solution(scoville, K):
    answer = 0
    for _ in range(len(scoville)-1):
        answer += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        value = a + b*2
        heapq.heappush(scoville, value)
        if min(scoville) >= k:
            return answer
    return -1

scoville = [1, 2, 3, 9, 10, 12]	
k = 7
print(solution(scoville, k))