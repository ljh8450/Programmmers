def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = list()
    l = 0
    while len(truck_weights) > 0:
        for i in range(bridge_length):
            if weight <= sum(truck_weights[0:i+1]):
                l = i
            else:
                break
        if len(queue) != 0:
            queue = list()
        if l >= len(truck_weights):
            return answer + 1
        queue = truck_weights[:l+1]
        truck_weights = truck_weights[l:]
        answer += 1

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))