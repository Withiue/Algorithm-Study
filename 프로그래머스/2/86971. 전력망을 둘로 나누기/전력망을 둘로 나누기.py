from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n + 1)]

    # 양방향 인접 리스트 만들기
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    answer = n

    # 전선을 하나씩 끊어 보기
    for a, b in wires:
        visited = [False] * (n + 1)
        visited[a] = True
        queue = deque([a])
        count = 0

        # a가 속한 전력망의 송전탑 개수 세기
        while queue:
            cur = queue.popleft()
            count += 1

            for nxt in graph[cur]:
                # 끊은 전선은 지나가지 않기
                if (cur == a and nxt == b) or (cur == b and nxt == a):
                    continue

                if not visited[nxt]:
                    visited[nxt] = True
                    queue.append(nxt)

        # 두 전력망의 송전탑 개수 차이
        difference = abs(count - (n - count))
        answer = min(answer, difference)

    return answer