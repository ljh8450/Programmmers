def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        temp = 0
        for j in range(i+1, len(prices)):
            temp += 1
            if prices[i] > prices[j]:
                break
        answer[i] = temp
    return answer