# 최소 객실 사용하여 손님 받기
# 퇴실 수 10분간 청소
# 최소 객실 수 return

# 빠른 시간 순으로 정렬해서 시작하기
# 끝나고 10분 뒤에 들어갈 수 있는, 시작 시간이 가장 작은 예약손님 구하기
# ㄴ 가능한 시작 시간이 없을 때 까지 반복

def solution(book_time):    
    # 분으로 모조리 바꾸기
    book_time_m = []
    for start_time, end_time in book_time:
        s_h, s_m = map(int, start_time.split(':'))
        e_h, e_m = map(int, end_time.split(':'))
        book_time_m.append([s_h*60 + s_m, e_h*60 + e_m])
    
    book_time_m.sort()  # 오름차순 정렬
    
    # 방 하나 배정
    rooms_p_time = [0]  # 각 방별로 다음 손님 받을 수 있는 시간(가능 시작 시간)
    
    for s, e in book_time_m:
        # 방에 해당 예약이 들어갈 수 있는지 확인
        for i in range(len(rooms_p_time)):
            # 방의 시작 가능 시간보다 현재 손님의 시작 시간이 더 빠르면 pass
            if rooms_p_time[i] > s: continue
            # 다음 손님 예약 가능하면 예약하기
            rooms_p_time[i] = e + 10
            break  # 방 순회 for문 탈출
        
        # 지금 있는 모든 방에 들어갈 곳이 없으면 새 방 주기
        else:
            rooms_p_time.append(e + 10)
            
    return len(rooms_p_time)