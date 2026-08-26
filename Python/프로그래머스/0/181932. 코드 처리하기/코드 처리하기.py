def solution(code):
    mode = 0
    result = ''
    for idx in range(len(code)):
        match mode:
            case 0:
                if code[idx] == "1":
                    mode = 1
                else:
                    if idx % 2 == 0:
                        result += code[idx]                        
            case 1:
                if code[idx] == "1":
                    mode = 0
                else:
                    if idx % 2 == 1:
                        result += code[idx]
    if not result:
        return "EMPTY"
    return result