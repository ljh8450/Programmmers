def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_num in phone_book:
        hash_map[phone_num] = 1
    for phone_num in phone_book:
        temp = ""
        for num in phone_num:
            temp += num
            if temp != phone_num and temp in hash_map:
                answer = False
    return answer