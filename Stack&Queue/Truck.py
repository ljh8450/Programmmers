def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = []
    while len(truck_weights) > 0:
        answer += 1
        if bridge_length > len(queue):
            if weight > sum(queue)+truck_weights[0]:
                queue.append(truck_weights.pop(0))
        else:
            queue.pop()
    return answer
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))