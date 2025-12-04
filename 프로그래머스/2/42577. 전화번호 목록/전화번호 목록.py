def solution(phone_book):
    phone_dict = {}
    for number in phone_book:
        phone_dict[number] = 1

    for number in phone_book:
        for i in range(1, len(number)):
            prefix = number[:i]
            if prefix in phone_dict:
                return False
    return True