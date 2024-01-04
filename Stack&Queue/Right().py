def solution(s):
    stack = []
    
    for c in s:
        if c == "(": #'('면 스택에 저장.
            stack.append(c)
        else: # 아니면 stack에 '('가 있다면 제거해서 다음 부분 탐색. 아니면 false
            if stack == []:
                return False
            else:
                stack.pop()
    return stack == []