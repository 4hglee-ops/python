def solution(myString, pat):
    save_string = myString[::-1]
    save_pat = pat[::-1]
    save_idx = save_string.find(save_pat)
    return myString[:len(myString)-(save_idx)]

