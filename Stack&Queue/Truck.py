def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = []
    while len(truck_weights) > 0:
        if bridge_length > len(queue):
            queue.append(truck_weights.pop(0))
            answer += 1
        else:
            queue.pop()
            answer += 1
    return answer
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))