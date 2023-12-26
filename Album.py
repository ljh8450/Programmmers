def solution(genres, plays):
    hash_map = {}
    count_map = {}
    answer = []
    for music in range(len(plays)):
        if genres[music] not in hash_map:
            hash_map[genres[music]] = [plays[music]]
        else:
            if len(hash_map[genres[music]]) == 1:
                hash_map[genres[music]].append(plays[music])
            elif len(hash_map[genres[music]]) == 2:
                hash_map[genres[music]].remove(min(hash_map[genres[music]]))
                hash_map[genres[music]].append(plays[music])
    for gen in list(hash_map.keys()):
        count_map[gen] = sum(hash_map[gen])
    count_map = sorted(count_map.items(), reverse = True)

    for hash_values in len(plays):
        if hash_values > len(hash_map.values()):
            return answer
        for i in range(len(plays)):
            if plays[i] == hash_map.values()[hash_values] and genres[i] == hash_map.keys[hash_values//2]:
                answer.append(i)
    
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))