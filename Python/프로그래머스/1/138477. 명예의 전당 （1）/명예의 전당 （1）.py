# 순서대로 저장
# 맨 마지막꺼 answer에 저장

# 인데 시간복잡도 상관없으니까 append 하고 정렬

def solution(k, score):
    answer = []
    score_rank = []
    i = 0
    for s in score:
        score_rank.append(s)
        score_rank.sort(reverse=True)
        answer.append(score_rank[:k][-1])                
        
    return answer