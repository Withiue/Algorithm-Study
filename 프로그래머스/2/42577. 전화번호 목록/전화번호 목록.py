def solution(phone_book):
    phone_book.sort()  # 정렬해서 인접한 전화번호만 탐색하기
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True