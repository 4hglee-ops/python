def solution(a, b, c, d):
    answer = 0
    dice_dict = {1 : 0,2 : 0,3 : 0,4 : 0,5 : 0,6 : 0}
    dice_cnt =  {0 : [],1 : [],2 : [],3 : [],4 : []}
    dice_dict[a] += 1
    dice_dict[b] += 1
    dice_dict[c] += 1
    dice_dict[d] += 1
    
    for idx,cnt in dice_dict.items():
        dice_cnt[cnt].append(idx)
        
    if dice_cnt[4]:
        return 1111*dice_cnt[4][0]
    elif dice_cnt[3]:
        return (10*dice_cnt[3][0]+dice_cnt[1][0])**2
    elif len(dice_cnt[2]) == 2:
        return (dice_cnt[2][0]+dice_cnt[2][1])*abs(dice_cnt[2][0]-dice_cnt[2][1])
    elif dice_cnt[2]:
        return dice_cnt[1][0]*dice_cnt[1][1]
    else:
        return dice_cnt[1][0]     
    
    return answer