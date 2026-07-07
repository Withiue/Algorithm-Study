def solution(rank, attendance):
    possible_student = sorted([rank[i] for i in range(len(rank)) if attendance[i]])
    
    a, b, c = rank.index(possible_student[0]), rank.index(possible_student[1]), rank.index(possible_student[2])
    
    return 10000 * a + 100 * b + c