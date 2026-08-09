def solution(sizes):
    com_w = 0
    com_h = 0
    max_w = 0
    max_h = 0
    for size in sizes:
        com_w = max(size[0],size[1])
        com_h = min(size[0],size[1])
        max_w = max(max_w,com_w)
        max_h = max(max_h,com_h)
        
    
    return max_w*max_h