from collections import deque
def solution(scoville, K):
    answer = 0
    scoville = deque(scoville)
    for _ in range(len(scoville)):
        answer += 1
        scoville = deque(sorted(scoville))
        a = scoville.popleft()
        b = scoville.popleft()
        scoville.append(a + b*2)
        if len(scoville) == 1:
            return -1

scoville = [1, 2, 3, 9, 10, 12]	
K = 7
print(solution(scoville, K))