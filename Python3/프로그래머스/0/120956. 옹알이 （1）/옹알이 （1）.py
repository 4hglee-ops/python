#오류 : 슬라이싱 끝까지를 [n:-1]로 입력, [n:]으로 해야함
def solution(babbling):
    answer = 0
    data = ["aya", "ye", "woo", "ma"]
    copy_bab = ''
    
    for text in babbling:
        copy_bab = text
        while True:
            if copy_bab[0:2] in data:
                if len(copy_bab) == 2:
                    answer += 1
                    break
                else:
                    copy_bab = copy_bab[2:]
            elif copy_bab[0:3] in data:
                if len(copy_bab) == 3:
                    answer += 1
                    break
                else:
                    copy_bab = copy_bab[3:]
            else:
                break
    
    return answer