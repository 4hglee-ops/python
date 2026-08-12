def solution(answers):
    answer = []
    supoza1 = [1,2,3,4,5]
    supoza2 = [2,1,2,3,2,4,2,5]
    supoza3 = [3,3,1,1,2,2,4,4,5,5]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    for idx,a in enumerate(answers):
        if a == supoza1[idx%len(supoza1)]:
            cnt1 += 1
        if a == supoza2[idx%len(supoza2)]:
            cnt2 += 1
        if a == supoza3[idx%len(supoza3)]:
            cnt3 += 1
    
    max_cnt = max(cnt1,cnt2,cnt3)
    if cnt1 == max_cnt:
        answer.append(1)
    if cnt2 == max_cnt:
        answer.append(2)
    if cnt3 == max_cnt:
        answer.append(3)    
    
    
    
    return answer