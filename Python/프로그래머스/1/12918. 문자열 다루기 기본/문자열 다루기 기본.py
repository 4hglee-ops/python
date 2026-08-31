def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for check in s:
        if not check.isdigit():
            return False
    return True