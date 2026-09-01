# 저장변수에 있는지 없는지 검사하고 있으면 길이 찾고, 없으면 넣고 결과에 -1 append
# 가장 가까운 곳에 있는 같은 글자 길이 알고리즘
# 현재위치까지 슬라이싱 후 거꾸로 접근해서 같은 문자 찾고 해당인덱스와 차이만큼 append

def solution(s):
    answer = []
    stack = ''
    
    for idx, text in enumerate(s):
        text_len = 0
        if text not in stack:
            stack += text
            answer.append(-1)
        else:
            s_slice = s[:idx][::-1]
            for i, s_s in enumerate(s_slice):
                if s_s == text:
                    answer.append(i+1)
                    break
    return answer