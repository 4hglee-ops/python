def solution(str_list):
    check_l = 0
    check_r = 0
    if "l" in str_list:
        check_l = 1
    if "r" in str_list:
        check_r = 1
    check_sum = check_l+check_r
    match check_sum:
        case 0:
            return []
        case 1:
            if check_l:
                find_l = str_list.index("l")
                return str_list[:find_l]
            else:
                find_r = str_list.index("r")
                return str_list[find_r+1:]
        case 2:
            find_l = str_list.index("l")
            find_r = str_list.index("r")
            if find_l < find_r:
                return str_list[:find_l]
            else:
                return str_list[find_r+1:]