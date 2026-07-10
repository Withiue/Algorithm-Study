# 구명보트 한 번에 최대 2명씩 탈 수 있음
# 구명보트 무게 제한 초과 불가능
# 구명보트 최소한으로 사용하여 모든 사람 구출

# 가장 무거운 사람은 무조건 태운다
# 이 상태에서 가장 가벼운 사람이 같이 탈 수 있는지 확인
# -> 가벼운 사람 못타면 혼자 타기


def solution(people, limit):
    answer = 0
    people.sort()
    light = 0
    heavy = -1
    for i in range(len(people)):
        if light > len(people) + heavy:
            break
        
        # 가장 무거운 사람 혼자 타는 경우
        if people[heavy] + people[light] > limit:
            pass
        # 가장 가벼운 사람도 같이 탈 수 있는 경우
        elif people[heavy] + people[light] <= limit:
            light += 1
        heavy -= 1
        answer += 1
    return answer