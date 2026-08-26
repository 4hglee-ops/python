def solution(myString, pat):
    answer = 0
    for idx, string in enumerate(myString):
        if pat in myString[idx:idx+len(pat)]:
            answer += 1    
            
    return answer