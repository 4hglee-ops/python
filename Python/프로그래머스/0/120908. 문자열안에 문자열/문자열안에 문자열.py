def solution(str1, str2):
    answer = 0
    for i in range(len(str1)):
        if str1[i:len(str2)+i]==str2:
            answer = 1
    if answer != 1:
        answer = 2
    return answer