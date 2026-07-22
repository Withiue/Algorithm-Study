
def solution(numbers):
    result = [-1] * len(numbers)
    stk = []
    
    for i in range(len(numbers)):
        # 현재 숫자가 이전 숫자의 답인지 확인
        while stk and numbers[stk[-1]] < numbers[i]:  # 크다면 뒤큰수이다.
            idx = stk.pop()
            result[idx] = numbers[i]
                
        # 아직 현재 숫자의 뒤큰수는 모르니까 stk에 넣기
        stk.append(i)
                
    
    return result
            
    