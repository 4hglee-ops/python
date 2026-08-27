def solution(rank, attendance):
    answer = 0
    student = {}
    for idx,att in enumerate(attendance):
        if att:
            student[rank[idx]] = idx
    student = sorted(student.items())
    return student[0][1]*10000+student[1][1]*100+student[2][1]
