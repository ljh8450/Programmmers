def solution(s):
    answer = True
    index = 0
    data = [e for e in s]
    if s[-1] == "(" or s[0] == ")" or "()" not in s:
        return False
    while len(data) > 0:
        if data[index]+data[index+1] == "()":
            data.pop(index)
            data.pop(index)
            index = 0
        else:
            index += 0
            if data[-1] == "(" or data[0] == ")" or ("()" not in data and len(data)>0):
                return False
        print(data)
    return True
