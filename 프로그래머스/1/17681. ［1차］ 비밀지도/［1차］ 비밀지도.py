def solution(n, arr1, arr2):
    answer = []
    # 두 장의 지도 OR 연산하기 -> 전체 지도
    for i in range(n):
        # OR 연산
        tmp_map = bin(arr1[i] | arr2[i])[2:].zfill(n)  # zfill(n): 앞을 0으로 채움, 총 n자릿수
        # '1'을 '#'으로, '0'을 ' '으로 변환해서 answer에 넣기
        tmp_map = tmp_map.replace('1', '#')
        tmp_map = tmp_map.replace('0', ' ')
        answer.append(tmp_map)
    return answer