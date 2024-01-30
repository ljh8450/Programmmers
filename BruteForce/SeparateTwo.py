from collections import deque
def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    res = 0
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(start):
        q = deque([start])
        cnt = 1
        visited = [0] * (n+1)
        visited[start] = 1
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
                    cnt += 1
        return cnt
    res = n
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        res = min(abs(bfs(a)-bfs(b)), res)

        graph[a].append(b)
        graph[b].append(a)
    return res

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

print(solution(n, wires))