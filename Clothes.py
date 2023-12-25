clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
answer = 1
plus = 0
hash_map = {}
check_map = {}
for i in range(len(clothes)):
    hash_map[clothes[i][1]] = clothes[i][0]
    check_map[clothes[i][1]] = 1
for j in range(len(clothes)):
    if check_map[clothes[j][1]] != 1:
        plus += 1
        answer *= len(check_map[clothes[j]])
answer += plus
print(answer)