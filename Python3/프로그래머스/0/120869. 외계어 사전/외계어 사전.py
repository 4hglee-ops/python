# def solution(spell, dic):
#     for text in dic:
#         count = 0
#         if len(spell)==len(text):
#             for sp in spell:
#                 if sp in text:
#                     count += 1
#             if len(spell) == count:
#                 return 1
            
#     return 2

def solution(spell, dic):
    for text in dic:
        count = 0
        for sp in spell:
            if sp in text:
                count += 1
        if len(spell) == count:
            return 1
            
    return 2