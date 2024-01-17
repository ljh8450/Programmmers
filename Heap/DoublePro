import heapq
def solution(operations):
    heap = []
    for o in operations:
        x, n = o.split()
        n = int(n)
        if x == "I":
            heapq.heappush(heap, n)
        elif n == 1:
            if len(heap) > 0:
                max_value = max(heap)
                heap.remove(max_value)
        else:
            if len(heap) > 0:
                min_value = heapq.heappop(heap)
    if heap:
        return [max(heap), heapq.heappop(heap)]
    else:
        return[0, 0]
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))