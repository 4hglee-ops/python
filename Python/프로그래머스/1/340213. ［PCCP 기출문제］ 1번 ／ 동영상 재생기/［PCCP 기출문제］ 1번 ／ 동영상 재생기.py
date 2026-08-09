def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_sec = str_to_sec(video_len)
    pos_sec = str_to_sec(pos)
    ops_sec = str_to_sec(op_start)
    ope_sec = str_to_sec(op_end)
    pos_sec = op_compare(pos_sec,ops_sec,ope_sec)

    for command in commands:
        if command == 'prev':
            pos_sec -= 10
            if pos_sec < 0:
                pos_sec = 0
        elif command == 'next':
            pos_sec += 10
            if pos_sec > video_sec :
                pos_sec = video_sec
        pos_sec = op_compare(pos_sec,ops_sec,ope_sec)
    
    answer = sec_to_str(pos_sec)

    return answer

def str_to_sec(text):
    result = 0
    result = int(text[0:2])*60 + int(text[3:5])
    return result

def sec_to_str(number):
    result = ''
    m = int(number) // 60
    s = int(number) % 60
    if int(number) < 0:
        return "00:00"
    if m >= 10 :
        result += str(m)+":"
    elif 0 <= m < 10 :
        result += "0"+str(m)+":"
    if s >= 10 :
        result += str(s)
    elif 0 <= s < 10 :
        result += "0"+str(s)
    return result

def op_compare(pos,start,end):
    if start<=pos<=end:
        return end
    else :
        return pos

