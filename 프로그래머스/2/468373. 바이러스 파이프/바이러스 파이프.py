from collections import deque


def solution(n, infection, edges, k):
    # graph[node] = [(연결된 노드, 파이프 타입), ...]
    graph = [[] for _ in range(n + 1)]

    for x, y, pipe_type in edges:
        graph[x].append((y, pipe_type))
        graph[y].append((x, pipe_type))

    # 선택한 종류의 파이프를 열었을 때 감염 확산
    def spread(pipe_type, infected):
        next_infected = infected[:]
        queue = deque()

        # 현재 감염된 모든 배양체에서 동시에 시작
        for node in range(1, n + 1):
            if next_infected[node]:
                queue.append(node)

        while queue:
            current = queue.popleft()

            for next_node, edge_type in graph[current]:
                # 이번에 선택한 종류의 파이프만 통과
                if edge_type != pipe_type:
                    continue

                # 이미 감염된 배양체라면 다시 방문하지 않음
                if next_infected[next_node]:
                    continue

                next_infected[next_node] = True
                queue.append(next_node)

        return next_infected

    # k번 동안 열 파이프의 순서를 완전탐색
    def select_pipe(depth, infected):
        if depth == k:
            return sum(infected)

        max_infected_count = 0

        for pipe_type in [1, 2, 3]:
            next_infected = spread(pipe_type, infected)

            infected_count = select_pipe(
                depth + 1,
                next_infected
            )

            max_infected_count = max(
                max_infected_count,
                infected_count
            )

        return max_infected_count

    # 최초 감염 상태
    infected = [False] * (n + 1)
    infected[infection] = True

    return select_pipe(0, infected)