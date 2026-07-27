def solution(files):
    
    def get_key(f):
        for i in range(len(f)):
            if f[i].isdigit():
                j = i
            
                while j < len(f) and f[j].isdigit():
                    j += 1

                head = f[:i].lower()
                number = int(f[i:j])

                return (head, number)
                
    # HEAD 기준으로 사전 순 정렬, 대소문자 구분 하지 않음
    files.sort(key=get_key)
    return files