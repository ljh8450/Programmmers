def solution(number, k):
    answer = ''
    def delNum(number):
        retNum = 0
        for i in range(len(number)):
            print(number[:i]+number[i:])
        #     retNum = max(retNum, int(number[:i]+number[i:]))
        # return chr(retNum)
    
    for i in range(k):
        number = delNum(number)
    # answer = number
    # return answer

number = "1924"
k = 2

# print(solution(number, k))
solution(number, k)