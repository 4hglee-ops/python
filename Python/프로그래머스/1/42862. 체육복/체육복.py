def solution(n, lost, reserve):
    answer = 0
    cnt = []
    max_idx = n-1
    for i in range(n):
        cnt.append(1)
        if i+1 in reserve:
            cnt[i] += 1
        if i+1 in lost:
            cnt[i] -= 1
    for i in range(n):
        if cnt[i] == 0:
            if i == 0:
                if cnt[i+1] > 1:
                    cnt[i]+=1
                    cnt[i+1]-=1
            elif i == max_idx:
                if cnt[i-1] > 1:
                    cnt[i]+=1
                    cnt[i-1]-=1
            else:
                if cnt[i-1] > 1:
                    cnt[i]+=1
                    cnt[i-1]-=1
                elif cnt[i+1] > 1:
                    cnt[i]+=1
                    cnt[i+1]-=1
    for i in range(n):
        if cnt[i] > 0:
            answer += 1
        
    return answer