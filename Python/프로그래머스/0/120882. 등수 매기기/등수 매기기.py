def solution(score):
    answer = []
    score2 = []
    score2_sort = []
    score_dict = {}
    for s in score:
        score2.append(s[0]+s[1])
    score2_sort = sorted(score2,reverse=True)
    for idx,sor in enumerate(score2_sort):
        score_dict[sor] = 0
    for idx,sor in enumerate(score2_sort):
        if score_dict[sor] == 0:
            score_dict[sor] = idx+1
    for s in score2:
        answer.append(score_dict[s])
        
    return answer