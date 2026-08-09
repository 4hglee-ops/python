'''
bandage [시전시간, 초당 회복량, 추가 회복량] 1차원 정수 배열
health 최대 체력을 의미하는 정수
attacks[i] [공격하는시간,피해량] 공격시간을 기준으로 오름차순 정렬된 상태 2차원 정수 배열
1. 어택 시간, 피해량 분류
'''
def solution(bandage, health, attacks):
    answer = 0
    now_hp = health
    bandage_time = 0
    attack_time = []
    attack_damage = []
    for i in range(len(attacks)):
        attack_time.append(attacks[i][0])
        attack_damage.append(attacks[i][1])
    for j in range(attack_time[-1]+1):
        if j in attack_time :
            now_hp -= attack_damage[attack_time.index(j)]
            if now_hp <= 0 :
                return -1
            bandage_time = 0
        elif j > 0 :
            now_hp = healing(health,now_hp,bandage[1])
            bandage_time += 1
            if bandage_time==int(bandage[0]):
                now_hp = healing(health,now_hp,bandage[2])
                bandage_time = 0
            
                                   

    answer = now_hp
    return answer

def healing(max_hp,pos,heal):
    if max_hp < pos+heal :
        return max_hp
    else :
        return pos + heal
    
