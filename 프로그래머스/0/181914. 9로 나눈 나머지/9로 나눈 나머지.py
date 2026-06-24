def solution(number):
    if number == '0':
        return 0
    
    number_sum = sum([int(c) for c in number])
    
    return number_sum % 9