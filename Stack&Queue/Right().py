def solution(s):
    answer = True
    index = 0
    data = [e for e in s]
    if s[-1] == "(" or s[0] == ")" or "()" not in s:
        answer = False
        return answer
    while len(s) > 0:
        if data[index]+data[index+1] == "()":
            data.pop(index)
            index = 0
        else:
            index += 0
    return answer

        

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer

s = "()()"
print(solution(s))
