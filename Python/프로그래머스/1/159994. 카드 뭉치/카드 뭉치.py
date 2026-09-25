# 순서와 만들 수 있는지 여부 확인
# index 구한 뒤 index 끼리 값 비교

def solution(cards1, cards2, goal):
    idx1 = 0
    idx2 = 0
    for g in goal:
        if idx1 < len(cards1) and g == cards1[idx1]:
            idx1 = idx1+1
        elif idx2 < len(cards2) and g == cards2[idx2]:
            idx2 = idx2+1
        else:
            return "No"
    return "Yes"

# def solution(cards1, cards2, goal):
#     answer = 'Yes'
#     cards1_idx_list = []
#     cards2_idx_list = []
#     cards1_idx_sort = []
#     cards2_idx_sort = []
    
#     for c1 in cards1:
#         cards1_idx_list.append(goal.index(c1))

#     for c2 in cards2:
#         cards2_idx_list.append(goal.index(c2))
    
#     cards1_idx_sort = sorted(cards1_idx_list)
#     cards2_idx_sort = sorted(cards2_idx_list)
    
#     if cards1_idx_list != cards1_idx_sort or cards2_idx_list != cards2_idx_sort :
#         return 'No'
#     for g in goal:
#         if g in cards1 or g in cards2:
#             pass
#         else:
#             return 'No'
#     return answer