def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        ans = num_list[0]
        for num in num_list[1:]:
            ans *= num
        return ans