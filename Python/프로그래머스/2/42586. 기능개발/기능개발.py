def solution(progresses, speeds):
    answer = [0]
    answer_idx = 0
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        while progresses and progresses[0]>=100:
            answer[answer_idx] += 1
            del progresses[0]
            del speeds[0]
        else:
            if progresses and answer[answer_idx] != 0:
                answer.append(0)
                answer_idx += 1
                        
    
    return answer