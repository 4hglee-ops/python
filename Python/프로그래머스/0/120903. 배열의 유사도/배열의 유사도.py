def solution(s1, s2):
    answer = 0
    s1_len = len(s1)
    s2_len = len(s2)
    for i in range(s1_len):
        for j in range(s2_len):
            if s1[i]==s2[j]:
                answer += 1
    return answer