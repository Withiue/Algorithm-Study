def solution(record):
    answer = []
    uid_dict = {}
    
    # 1. 각 최종 닉네임 저장
    for r in record:
        data = r.split()
        
        action = data[0]
        uid = data[1]
        
        if action == 'Enter' or action == 'Change':
            nickname = data[2]
            uid_dict[uid] = nickname
    
    # 2. 기록대로 출력하기
    for r in record:
        data = r.split()
        
        action = data[0]
        uid = data[1]
        
        if action == 'Enter':
            answer.append(f"{uid_dict[uid]}님이 들어왔습니다.")
        
        elif action == 'Leave':
            answer.append(f"{uid_dict[uid]}님이 나갔습니다.")
        
    return answer