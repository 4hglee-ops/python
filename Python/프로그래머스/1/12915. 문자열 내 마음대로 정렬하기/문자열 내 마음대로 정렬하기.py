def solution(strings, n):
    answer = []
    strings.sort()
    strings_list = []
    for string in strings:
        strings_list.append([string[n],string])
    strings_list.sort()
    for s in strings_list:
        answer.append(s[1])
    return answer