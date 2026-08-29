def solution(m, musicinfos):
    
    # C#, D# 같은 음을 한 글자로 치환
    def replace_sharp(s):
        return (s.replace('C#', 'c')
                 .replace('D#', 'd')
                 .replace('F#', 'f')
                 .replace('G#', 'g')
                 .replace('A#', 'a')
                 .replace('B#', 'b'))
    
    m = replace_sharp(m)
    
    answer = "(None)"
    max_time = -1
    
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        
        # 재생 시간 계산
        sh, sm = map(int, start.split(':'))
        eh, em = map(int, end.split(':'))
        
        play_time = (eh * 60 + em) - (sh * 60 + sm)
        
        # 악보의 # 처리
        melody = replace_sharp(melody)
        
        # 실제 재생된 멜로디 만들기
        played = ''
        
        for i in range(play_time):
            played += melody[i % len(melody)]
        
        # 기억한 멜로디가 포함되어 있는지 확인
        if m in played:
            # 재생 시간이 더 긴 음악만 갱신
            # 같은 시간이면 먼저 나온 음악을 유지
            if play_time > max_time:
                max_time = play_time
                answer = title
    
    return answer