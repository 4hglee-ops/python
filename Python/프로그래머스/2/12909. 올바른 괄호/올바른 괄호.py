def solution(s):
    answer = True
    stack = []
    if s[0] == ')':
        return False
    for t in s:
        if t == '(':
            stack.append(t)
        elif t == ')':
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    
    return True