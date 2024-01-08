from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    current_weight = 0

    while len(truck_weights) > 0:
        answer += 1
        current_weight -= queue.popleft()

        if weight >= truck_weights[0] + current_weight:
            current_weight += truck_weights[0]
            queue.append(truck_weights.popleft())
        else:
            queue.append(0)
    answer += bridge_length           
    return answer