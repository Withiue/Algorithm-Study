def solution(edges):
    answer = [0, 0, 0, 0]

    # 각 정점의 들어오는 간선 수와 나가는 간선 수
    in_degree = {}
    out_degree = {}

    for start, end in edges:
        out_degree[start] = out_degree.get(start, 0) + 1
        in_degree[end] = in_degree.get(end, 0) + 1

        # 딕셔너리에 없는 정점도 0으로 등록
        in_degree.setdefault(start, 0)
        out_degree.setdefault(end, 0)

    created = 0      # 생성한 정점
    stick_count = 0  # 막대 그래프
    eight_count = 0  # 8자 그래프

    for node in in_degree:
        # 들어오는 간선은 없고, 나가는 간선이 2개 이상
        if in_degree[node] == 0 and out_degree[node] >= 2:
            created = node

        # 나가는 간선이 없으면 막대 그래프의 마지막 정점
        elif out_degree[node] == 0:
            stick_count += 1

        # 들어오는 간선과 나가는 간선이 각각 2개 이상이면
        # 8자 그래프의 가운데 정점
        elif in_degree[node] >= 2 and out_degree[node] == 2:
            eight_count += 1

    # 생성한 정점의 나가는 간선 수 = 전체 그래프 개수
    total_count = out_degree[created]

    # 전체 그래프 = 도넛 + 막대 + 8자
    donut_count = total_count - stick_count - eight_count

    answer[0] = created
    answer[1] = donut_count
    answer[2] = stick_count
    answer[3] = eight_count

    return answer