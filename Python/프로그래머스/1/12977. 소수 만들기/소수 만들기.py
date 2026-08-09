# 숫자조합 리스트에 넣고
# 리스트에 넣은거 소수확인해서 +1

def solution(nums):
    answer = 0

    sum_nums = []
    i=0
    j=1
    k=2

    while True:
        sum_nums.append(nums[i]+nums[j]+nums[k])

        if nums[i] == nums[-3]:
            break
        if j == len(nums)-2:
            i+=1
            j=i+1
            k=i+2    
        elif k == len(nums)-1:
            j+=1
            k=j+1
        else :
            k+=1

    for num in sum_nums:
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                break
        else :
            answer += 1
            
    print(sum_nums)
    return answer