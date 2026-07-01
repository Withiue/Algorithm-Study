from collections import defaultdict

def solution(id_list, report, k):
    user_list = defaultdict(set)  # 유저와 유저가 신고한 타 유저들, 중복 제외
    cnt_user = defaultdict(int) # 신고당한 유저
      
    report = list(set(report))  # 한 유저가 같은 유저를 여러 번 신고한 경우를 set으로 제외시킨다
    
    # 유저 몇 번 신고당했는지
    for users in report:
        user_from, user_to = users.split()  # 신고한 유저, 신고당한 유저
        user_list[user_from].add(user_to)  # 신고한 유저가 누구를 신고했는지 더하기
        cnt_user[user_to] += 1  # 유저가 신고받은 회수 1회 더하기
    
    result = []
    for user in id_list:
        mail_cnt = 0  # 보낼 메일 수
        
        for reported_user in user_list[user]:  # 유저가 신고한 유저 하나씩 순회
            if cnt_user[reported_user] >= k:  # k번 이상 신고당한 유저라면
                mail_cnt += 1  # 보낼 메일 수에 +1 하기
                
        result.append(mail_cnt)  # 보낼 메일 수 다 카운트 하면 최종 리스트에 넣기
    
    return result