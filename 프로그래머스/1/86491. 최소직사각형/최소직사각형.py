# 1. 가로 길이가 항상 더 크게 정렬하기
# 2. 명함들의 정렬된 가로, 세로 길이 중 가장 큰 걸 가져가기
# 3. 지갑 크기를 구해서 return

def solution(sizes):
    sorted_sizes = [[max(size), min(size)] for size in sizes]
    width = max([size[0] for size in sorted_sizes])
    height = max([size[1] for size in sorted_sizes])
    return width * height