def solution(n):
    answer = [[]]
    for i in range(n):
        answer.append([0])
        if i==0:
            del answer[0]
        for j in range(n):
            if not j==n-1:
                answer[i].append(0)
            if i==j:
                answer[i][j]+=1
    
    return answer