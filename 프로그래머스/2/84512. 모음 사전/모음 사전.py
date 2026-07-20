def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    word_dict = []  # 모든 단어를 순서대로 만들어 넣을 변수
    
    # 모든 단어를 순서대로 만들어 사전에 넣기
    def make_dict(cur_word):
        # 만들어진 단어를 단어사전에 넣기
        if cur_word:
            word_dict.append(cur_word)

        # 길이가 5면(다 찼으면) return
        if len(cur_word) == 5:
            return

        for v in vowels:
            make_dict(cur_word + v)  # 다음 단어를 넣어서 다음 재귀로.
            
    make_dict('')
    
    return word_dict.index(word) + 1